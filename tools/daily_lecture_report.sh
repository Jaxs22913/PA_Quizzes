#!/bin/bash
# Daily lecture audit -> macOS notification + dated log.
#
# Runs from launchd so it survives Claude sessions, reboots and logouts. launchd
# cannot hold a conversation, so this is deliberately a NOTIFIER: it says what is
# missing and where the detail is. Ask Claude for the full picture any time.
#
# Silent when nothing is wrong and silent on days with no lectures — a daily ping
# that always fires is a daily ping you stop reading.
set -uo pipefail
REPO="/Users/jaxonluke/Developer/PA_Quizzes"
LOGDIR="$HOME/Library/Logs/pa-lecture-audit"
mkdir -p "$LOGDIR"
DAY=$(date +%Y-%m-%d)
OUT="$LOGDIR/$DAY.json"

cd "$REPO" || exit 0
/usr/bin/python3 tools/daily_lecture_audit.py > "$OUT" 2>"$LOGDIR/$DAY.err"

# Parse with python rather than jq, which is not installed by default.
SUMMARY=$(/usr/bin/python3 - "$OUT" <<'PY'
import json, sys
try:
    d = json.load(open(sys.argv[1]))
except Exception:
    print("ERR|audit did not produce readable output"); raise SystemExit
if d.get("lectures", 0) == 0:
    print("QUIET|"); raise SystemExit
if d.get("audio_check_blocked"):
    print("PERM|Slides checked OK, but the recording check is blocked. "
          "Grant Full Disk Access to /bin/bash in System Settings > Privacy.")
    raise SystemExit
gaps = []
for label, key in (("no slides", "missing_deck"), ("no audio", "missing_audio")):
    for item in d.get(key, []):
        who = item.split(" — ")[0]
        what = item.split(" — ")[-1]
        gaps.append("%s: %s (%s)" % (who, what[:44], label))
for x in d.get("unmatched_audio", []) + d.get("unmatched_files", []):
    gaps.append("unmatched: %s" % x[:60])
if gaps:
    print("GAP|" + "\n".join(gaps[:6]))
else:
    print("OK|%d lecture(s), all slides and audio present" % d["lectures"])
PY
)

STATE="${SUMMARY%%|*}"
BODY="${SUMMARY#*|}"
echo "$(date '+%F %T')  $STATE  ${BODY//$'\n'/ ; }" >> "$LOGDIR/history.log"

case "$STATE" in
  GAP)
    /usr/bin/osascript -e "display notification \"${BODY//\"/\\\"}\" with title \"PA lecture audit\" subtitle \"Missing material today\" sound name \"Ping\"" >/dev/null 2>&1
    ;;
  PERM)
    /usr/bin/osascript -e "display notification \"${BODY//\"/\\\"}\" with title \"PA lecture audit\" subtitle \"Needs permission\" sound name \"Ping\"" >/dev/null 2>&1
    ;;
  ERR)
    /usr/bin/osascript -e "display notification \"Audit failed to run — see $LOGDIR\" with title \"PA lecture audit\"" >/dev/null 2>&1
    ;;
  *) : ;;   # OK and QUIET stay silent on purpose
esac
exit 0
