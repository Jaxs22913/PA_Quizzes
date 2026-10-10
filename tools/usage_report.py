#!/usr/bin/env python3
"""Anonymous usage report for PA Quizzes: reads the daily count documents that metrics.js writes
(metrics_daily/{YYYY-MM-DD}) and prints a Markdown summary.

    python3 tools/usage_report.py                 # totals since launch, months, the last 8 weeks
    python3 tools/usage_report.py --weeks 16      # more weeks
    python3 tools/usage_report.py --since 2026-10-10
    python3 tools/usage_report.py --from-json f   # an exported copy instead of Firestore (tests)

READ ONLY. It sends GET requests and nothing else, and the credential it is meant to use is a
service account with only the "Cloud Datastore Viewer" role, so even a bug here could not write.
The key file lives OUTSIDE the repo: ~/.config/pa-quizzes/usage-reader.json (or $PA_USAGE_KEY).
Never commit it, paste it into a chat, or print it.

Small-number rule (Jaxon, 2026-10-10): any number derived from fewer than 10 distinct students is shown
as "fewer than 10". The documents hold no identities, so the base of a number is the distinct-student
count of its period: a month's numbers need 10+ students active that month, a week's 10+ that week, and
the since-launch totals 10+ in the busiest month (a lower bound on everyone who ever used it). A count
that is itself below 10 can only come from fewer than 10 students, so it is hidden too.

How distinct students are counted (metrics.js): each device adds 1 to "active this day / ISO week /
month" the first time it is used in that period, and a signed-in student's devices share that marker
through cloud sync, so they count once. A student who never signs in and uses two devices counts twice;
one who turned counting off is not counted at all. Today's numbers are partial: devices send their
counts at most every 10 minutes, or on their next visit.
"""
import argparse, datetime, json, os, pathlib, sys, urllib.parse, urllib.request

PROJECT = "pa-quizzes-addc1"
KEY = os.environ.get("PA_USAGE_KEY") or os.path.expanduser("~/.config/pa-quizzes/usage-reader.json")
VENV_PY = os.path.expanduser("~/Developer/pa-tools/venv/bin/python")
SMALL = 10

# Each family is one collection of day documents. "base" names the distinct counters of its population.
FAMILIES = [
    {
        "coll": "metrics_daily",
        "title": None,
        "base": {"d": "active_d", "w": "active_w", "m": "active_m"},
        "base_label": "Active students",
        "fields": [
            ("q_answered", "Questions answered"),
            ("quiz_done", "Quizzes completed"),
            ("guide_open", "Study guides opened"),
            ("cram_open", "Cram sheets opened"),
            ("ref_open", "Other reference pages opened"),
            ("arcade_session", "Arcade sessions"),
            ("review_drill", "Missed-question drills started"),
            ("planner_day", "Study planner days (a student using it on a day)"),
        ],
        "rate": None,
        "columns": ["q_answered", "quiz_done"],
    },
]


def need_google_auth():
    try:
        import google.auth  # noqa: F401
        return
    except ImportError:
        pass
    venv = os.path.dirname(os.path.dirname(VENV_PY))
    if os.path.exists(VENV_PY) and os.path.realpath(sys.prefix) != os.path.realpath(venv):
        os.execv(VENV_PY, [VENV_PY] + sys.argv)   # the pa-tools venv has google-auth
    sys.exit("usage_report.py needs google-auth: pip install google-auth requests")


def fetch(coll):
    """Every document of a collection, as {doc_id: {field: int}}. GET requests only."""
    from google.oauth2 import service_account
    from google.auth.transport.requests import Request
    if not os.path.exists(KEY):
        sys.exit("No read-only key at %s. See docs/USAGE_METRICS.md, 'Running the report'." % KEY)
    creds = service_account.Credentials.from_service_account_file(KEY, scopes=["https://www.googleapis.com/auth/datastore"])
    creds.refresh(Request())
    out, token = {}, None
    while True:
        q = {"pageSize": "300"}
        if token: q["pageToken"] = token
        url = "https://firestore.googleapis.com/v1/projects/%s/databases/(default)/documents/%s?%s" % (PROJECT, coll, urllib.parse.urlencode(q))
        req = urllib.request.Request(url, headers={"Authorization": "Bearer " + creds.token}, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                page = json.load(r)
        except urllib.error.HTTPError as e:
            sys.exit("Firestore said %s for %s: %s" % (e.code, coll, e.read()[:300].decode("utf8", "replace")))
        for d in page.get("documents", []):
            vals = {}
            for k, v in (d.get("fields") or {}).items():
                if "integerValue" in v: vals[k] = int(v["integerValue"])
                elif "doubleValue" in v: vals[k] = int(v["doubleValue"])
            out[d["name"].rsplit("/", 1)[1]] = vals
        token = page.get("nextPageToken")
        if not token: return out


def iso_week(day):
    y, w, _ = datetime.date.fromisoformat(day).isocalendar()
    return "%d-W%02d" % (y, w)


def week_span(wk):
    y, w = wk.split("-W")
    mon = datetime.date.fromisocalendar(int(y), int(w), 1)
    return "%s to %s" % (mon.strftime("%b %d"), (mon + datetime.timedelta(days=6)).strftime("%b %d"))


def shown(n, base):
    """The small-number rule."""
    if base < SMALL or n < SMALL: return "fewer than 10"
    return "{:,}".format(n)


def sums(docs, field, days):
    return sum(docs.get(d, {}).get(field, 0) for d in days)


def family_report(F, docs, weeks, lines):
    days = sorted(d for d in docs if len(d) == 10 and d[4] == "-")
    if not days:
        lines.append("No data yet in `%s`." % F["coll"]); lines.append(""); return
    months = sorted({d[:7] for d in days})
    month_base = {m: sums(docs, F["base"]["m"], [d for d in days if d[:7] == m]) for m in months}
    launch_base = max(month_base.values()) if month_base else 0
    wks = sorted({iso_week(d) for d in days})[-weeks:]
    week_base = {w: sums(docs, F["base"]["w"], [d for d in days if iso_week(d) == w]) for w in wks}

    if F["title"]: lines += ["## " + F["title"], ""]
    lines += ["### Since launch (%s to %s)" % (days[0], days[-1]), "", "| | Total |", "|---|---:|"]
    for f, label in F["fields"]:
        lines.append("| %s | %s |" % (label, shown(sums(docs, f, days), launch_base)))
    if F.get("rate"):
        up, down, label = F["rate"]
        n_up, n_dn = sums(docs, up, days), sums(docs, down, days)
        n = n_up + n_dn
        rate = "fewer than 10 ratings" if (n < SMALL or launch_base < SMALL) else "%d%% helpful (of %s ratings)" % (round(100.0 * n_up / n), "{:,}".format(n))
        lines.append("| %s | %s |" % (label, rate))
    lines.append("| %s in the busiest month | %s |" % (F["base_label"], shown(launch_base, launch_base)))
    lines.append("")

    cols = F["columns"]
    labels = dict(F["fields"])
    head = "| {} | {} | {} |".format("{}", F["base_label"], " | ".join(labels[c] for c in cols))
    lines += ["### By month", "", head.format("Month"), "|---|---:|" + "---:|" * len(cols)]
    for m in months:
        md = [d for d in days if d[:7] == m]
        b = month_base[m]
        lines.append("| %s | %s | %s |" % (datetime.date.fromisoformat(m + "-01").strftime("%B %Y"), shown(b, b),
                                           " | ".join(shown(sums(docs, c, md), b) for c in cols)))
    lines.append("")
    lines += ["### By week (last %d ISO weeks, Monday to Sunday)" % len(wks), "", head.format("Week"), "|---|---:|" + "---:|" * len(cols)]
    for w in wks:
        wd = [d for d in days if iso_week(d) == w]
        b = week_base[w]
        lines.append("| %s (%s) | %s | %s |" % (w, week_span(w), shown(b, b), " | ".join(shown(sums(docs, c, wd), b) for c in cols)))
    lines.append("")
    per_day = [docs[d].get(F["base"]["d"], 0) for d in days]
    avg = round(sum(per_day) / len(per_day))
    busiest = max(days, key=lambda d: docs[d].get(F["base"]["d"], 0))
    top = docs[busiest].get(F["base"]["d"], 0)
    lines.append("Daily: %d days with data; %s per day on average: %s; busiest day %s: %s." % (
        len(days), F["base_label"].lower(), shown(avg, avg), busiest, shown(top, top)))
    lines.append("")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--weeks", type=int, default=8)
    ap.add_argument("--since", help="ignore days before YYYY-MM-DD")
    ap.add_argument("--from-json", help='a file {"metrics_daily": {"2026-10-10": {...}}, ...} instead of Firestore')
    a = ap.parse_args()
    data = json.loads(pathlib.Path(a.from_json).read_text()) if a.from_json else None
    if data is None: need_google_auth()
    lines = ["# PA Quizzes usage report", "",
             "Generated %s. Anonymous daily totals only: no names, answers, accounts or devices are stored. "
             "Any number that comes from fewer than 10 distinct students reads \"fewer than 10\"." % datetime.date.today().isoformat(), ""]
    for F in FAMILIES:
        docs = data.get(F["coll"], {}) if data is not None else fetch(F["coll"])
        if a.since: docs = {d: v for d, v in docs.items() if d >= a.since}
        family_report(F, docs, a.weeks, lines)
    lines += ["### How these are counted", "",
              "- %s: each device counts once per day, ISO week and month, and a signed-in student's devices count once. "
              "A student who never signs in and uses two devices counts twice (so does one who clears their browser data); "
              "a student who turned counting off is not counted at all." % FAMILIES[0]["base_label"],
              "- Not counted: anyone who turned counting off in Settings, developer devices and accounts, automated browsers, local previews.",
              "- Today's row is partial: devices send their counts at most every 10 minutes, or on their next visit.", ""]
    print("\n".join(lines))


if __name__ == "__main__":
    main()
