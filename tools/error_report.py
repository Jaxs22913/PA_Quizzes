#!/usr/bin/env python3
"""Site error report: the error pings theme.js sends (2026-10-19), read back from Cloudflare.

theme.js turns each distinct script error on a page view into one request for
    /PA_Quizzes/_e/v1/<page kind>/<folder~page>/<file-line>/<message>
which 404s; Cloudflare's request analytics count the paths. This reads the last 8 days of them (UTC dates),
prints the latest day's errors, and marks the ones not seen on any of the 7 days before as NEW (an
issue is opened only when there is a NEW one).

    CF_ANALYTICS_TOKEN=... python3 tools/error_report.py            # print the report
    python3 tools/error_report.py --issue                            # also open a GitHub issue (Actions)
    python3 tools/error_report.py --day 2026-10-20                   # report a given UTC day

The token needs only Zone > Analytics > Read on pa-quizzes.com. Without it the script says so and exits 0,
so the daily workflow (.github/workflows/site-errors.yml) is harmless until the secret is added.
Self-test pings (message containing "pa-error-selftest") are listed separately and never open an issue.
"""
import argparse, datetime as dt, json, os, re, sys, urllib.parse, urllib.request

ZONE = "4df8842d0c5a29b5a78e0f9bc9585929"          # pa-quizzes.com
PREFIX = "/PA_Quizzes/_e/v1/"
QUERY = """query($zone:String!,$s:Time!,$e:Time!){viewer{zones(filter:{zoneTag:$zone}){
  e: httpRequestsAdaptiveGroups(limit:5000, filter:{datetime_geq:$s, datetime_lt:$e, clientRequestPath_like:"%s%%"},
     orderBy:[count_DESC]){ count dimensions{ clientRequestPath date } } }}}""" % PREFIX


def fetch(token, start, end):
    body = json.dumps({"query": QUERY, "variables": {"zone": ZONE, "s": start, "e": end}}).encode()
    req = urllib.request.Request("https://api.cloudflare.com/client/v4/graphql", data=body,
                                 headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        out = json.load(r)
    if out.get("errors"):
        raise SystemExit("Cloudflare GraphQL error: %s" % out["errors"])
    return out["data"]["viewer"]["zones"][0]["e"]


def parse(path):
    # Anyone can request any /_e/ path, so every field is cut down to the characters theme.js itself sends
    # before it goes into a report or a GitHub issue (no markdown, links, @mentions or new lines).
    segs = [re.sub(r"[^A-Za-z0-9 _.$'()~-]", "", urllib.parse.unquote(s))[:110] for s in path[len(PREFIX):].split("/")]
    segs += [""] * (4 - len(segs))
    kind, page, where, msg = segs[:4]
    return {"kind": kind, "page": page.replace("~", " / "), "where": where, "msg": msg.replace("-", " ")}


def known(sig):
    """The key for "seen before?": the file without its line number, so editing a file does not make every
    known error in it look new."""
    kind, page, where, msg = sig
    return (kind, page, re.sub(r"-\d+$", "", where), msg)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--day", help="UTC day to report (default: yesterday)")
    ap.add_argument("--issue", action="store_true", help="open a GitHub issue when there are real errors")
    a = ap.parse_args()
    token = os.environ.get("CF_ANALYTICS_TOKEN")
    if not token:
        print("CF_ANALYTICS_TOKEN is not set: nothing to read. (Add the repo secret to turn the daily report on.)")
        return 0
    day = dt.date.fromisoformat(a.day) if a.day else dt.datetime.now(dt.timezone.utc).date() - dt.timedelta(days=1)
    start, end = day - dt.timedelta(days=7), day + dt.timedelta(days=1)
    rows = fetch(token, start.isoformat() + "T00:00:00Z", end.isoformat() + "T00:00:00Z")

    today, before = {}, set()
    for r in rows:
        p, d, c = r["dimensions"]["clientRequestPath"], r["dimensions"]["date"], r["count"]
        info = parse(p)
        sig = (info["kind"], info["page"], info["where"], info["msg"])
        if d == day.isoformat():
            today[sig] = today.get(sig, 0) + c
        else:
            before.add(known(sig))
    # "in", not startswith: a browser self-test arrives as "Error pa error selftest ..." (the error's type comes first)
    real = {s: c for s, c in today.items() if "pa error selftest" not in s[3]}
    tests = {s: c for s, c in today.items() if s not in real}
    new = [s for s in real if known(s) not in before]

    lines = ["Site errors on %s (UTC): %d distinct, %d new, %d pings in all." % (day, len(real), len(new), sum(real.values())), ""]
    if real:
        lines += ["| | count | page kind | page | file-line | error |", "|---|---:|---|---|---|---|"]
        for s, c in sorted(real.items(), key=lambda kv: (kv[0] not in new, -kv[1])):
            lines.append("| %s | %d | %s | %s | %s | %s |" % ("**NEW**" if s in new else "", c, s[0], s[1], s[2], s[3].replace("|", "/")))
    if tests:
        lines += ["", "Self-test pings: %d (ignored)." % sum(tests.values())]
    lines += ["", "Counts are Cloudflare's (sampled at high volume). A ping is one page view's first sighting of that error."]
    report = "\n".join(lines)
    print(report)

    if a.issue and new:                     # known errors stay in the run log; only a NEW one opens an issue
        repo, gh = os.environ.get("GITHUB_REPOSITORY"), os.environ.get("GITHUB_TOKEN")
        if not (repo and gh):
            print("--issue needs GITHUB_REPOSITORY and GITHUB_TOKEN (set in Actions).")
            return 0
        title = "Site errors %s: %d new, %d distinct" % (day, len(new), len(real))
        req = urllib.request.Request("https://api.github.com/repos/%s/issues" % repo,
                                     data=json.dumps({"title": title, "body": report}).encode(),
                                     headers={"Authorization": "Bearer " + gh, "Accept": "application/vnd.github+json"})
        with urllib.request.urlopen(req, timeout=60) as r:
            print("opened", json.load(r).get("html_url"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
