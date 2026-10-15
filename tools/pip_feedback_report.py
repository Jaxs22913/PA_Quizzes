#!/usr/bin/env python3
"""Pip feedback report: the "Not helpful" reports students chose to send (pip/pip-window.js offerSend ->
Firestore pip_feedback). Each holds the student's question, Pip's answer as shown, an optional comment,
the exam, the kind of answer (pip = Pip's cards and guide passages, claude = a Claude explanation built on
the class passages, general = Claude's general-knowledge part) and the day. No names, emails or account ids
are stored, so nothing here says who sent what.

    python3 tools/pip_feedback_report.py                 # the last 14 days, newest first
    python3 tools/pip_feedback_report.py --days 60 --exam principles-of-diagnostic-medicine-i-exam-3
    python3 tools/pip_feedback_report.py --json out.json # everything, for a closer look

Uses the same read-only key as tools/usage_report.py (~/.config/pa-quizzes/usage-reader.json, role Cloud
Datastore Viewer; see docs/USAGE_METRICS.md). GET requests only: it never changes or deletes a report.
The rule that lets the site write them is in firestore.rules (match /pip_feedback); publish it in the
Firebase console first, or every send fails and students see "I couldn't send it just now".
"""
import argparse, collections, datetime, json, os, sys, textwrap
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import usage_report as U   # the key, the project and the venv re-exec live there


def fetch_all():
    """Every pip_feedback document as a dict of its string fields (Firestore REST, paged GETs)."""
    import urllib.parse, urllib.request
    from google.oauth2 import service_account
    from google.auth.transport.requests import Request
    if not os.path.exists(U.KEY):
        sys.exit("No read-only key at %s. See docs/USAGE_METRICS.md, 'Running the report'." % U.KEY)
    creds = service_account.Credentials.from_service_account_file(U.KEY, scopes=["https://www.googleapis.com/auth/datastore"])
    creds.refresh(Request())
    out, token = [], None
    while True:
        q = {"pageSize": "300"}
        if token:
            q["pageToken"] = token
        url = "https://firestore.googleapis.com/v1/projects/%s/databases/(default)/documents/pip_feedback?%s" % (U.PROJECT, urllib.parse.urlencode(q))
        req = urllib.request.Request(url, headers={"Authorization": "Bearer " + creds.token}, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                page = json.load(r)
        except urllib.error.HTTPError as e:
            sys.exit("Firestore said %s: %s" % (e.code, e.read()[:300].decode("utf8", "replace")))
        for d in page.get("documents", []):
            f = {k: v.get("stringValue", v.get("integerValue")) for k, v in (d.get("fields") or {}).items()}
            f["created"] = d.get("createTime", "")[:10]
            out.append(f)
        token = page.get("nextPageToken")
        if not token:
            return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--days", type=int, default=14)
    ap.add_argument("--exam", help="only this exam (its folder slug, as the report prints it)")
    ap.add_argument("--json", help="write every matching report to this file")
    a = ap.parse_args()
    U.need_google_auth()
    since = (datetime.date.today() - datetime.timedelta(days=a.days)).isoformat()
    rows = [r for r in fetch_all() if str(r.get("day", "")) >= since and (not a.exam or r.get("exam") == a.exam)]
    rows.sort(key=lambda r: (str(r.get("day", "")), r.get("created", "")), reverse=True)
    if a.json:
        with open(a.json, "w", encoding="utf-8") as fh:
            json.dump(rows, fh, ensure_ascii=False, indent=1)
    print("Pip feedback since %s: %d report%s" % (since, len(rows), "" if len(rows) == 1 else "s"))
    if not rows:
        return
    for title, key in (("by exam", "exam"), ("by kind of answer", "kind")):
        c = collections.Counter(r.get(key) or "?" for r in rows)
        print("  %s: %s" % (title, ", ".join("%s %d" % kv for kv in c.most_common())))
    w = textwrap.TextWrapper(width=100, initial_indent="      ", subsequent_indent="      ")
    for r in rows:
        print("\n%s  %s  [%s]" % (r.get("day"), r.get("exam") or "(no exam)", r.get("kind")))
        print("  Q: %s" % r.get("q", ""))
        if r.get("c"):
            print("  Comment: %s" % r["c"])
        print("  Pip said:")
        print(w.fill(str(r.get("a", ""))[:1200]))


if __name__ == "__main__":
    main()
