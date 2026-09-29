/* Study planner engine -- pure logic, no DOM, no storage. Runs in the browser
 * (window.PlannerEngine) and in Node (module.exports) so it can be unit tested.
 *
 * What it does
 *   1. turns the academic calendar into a list of exams, each knowing WHICH
 *      lectures it covers ("Exam #2 (4-8)") and the date every one of those
 *      lectures is actually delivered;
 *   2. turns each exam into "demand": minutes of study that may only start once
 *      the material exists (a lecture cannot be reviewed before it is taught),
 *      then repeat at spaced gaps, then a heavier final week;
 *   3. schedules all exams' demand together under a daily cap, nearest exam
 *      first, and reports honestly what does not fit;
 *   4. replays a forgiving streak from the day log.
 *
 * Why these rules (research, summarised in the tracker's help text)
 *   - Spaced practice and practice testing are the two best-supported study
 *     techniques (Dunlosky et al. 2013). The best gap between sessions is about
 *     20% of the time left before the test at a weeks-scale delay (Cepeda et
 *     al. 2008) -> `reviewGapPct`.
 *   - Cramming helps immediately and loses to spacing on delayed tests, so the
 *     ramp is gentle early and heavy late, with a light last day.
 *   - One missed day barely dents habit formation (Lally et al. 2010), and
 *     harsh streaks make people quit after a break -> free rest day + freezes.
 *
 * Every number below is a DEFAULT the student can change in the tracker's
 * advanced settings; nothing here is a claim that a given total is "right".
 */
(function (root, factory) {
  if (typeof module === "object" && module.exports) module.exports = factory();
  else root.PlannerEngine = factory();
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  /* ------------------------------------------------------------- dates -- */
  function pad(n) { return (n < 10 ? "0" : "") + n; }
  function parse(s) { var p = String(s).split("-"); return new Date(+p[0], +p[1] - 1, +p[2]); }
  function fmt(d) { return d.getFullYear() + "-" + pad(d.getMonth() + 1) + "-" + pad(d.getDate()); }
  function add(s, n) { var d = parse(s); d.setDate(d.getDate() + n); return fmt(d); }
  function diff(a, b) { return Math.round((parse(b) - parse(a)) / 864e5); }   // days from a to b
  function dow(s) { return parse(s).getDay(); }                                // 0 = Sunday
  function mondayOf(s) { var w = dow(s); return add(s, -((w + 6) % 7)); }
  function range(a, b) { var out = [], n = diff(a, b); for (var i = 0; i <= n; i++) out.push(add(a, i)); return out; }

  /* ---------------------------------------------------------- defaults -- */
  var DEFAULTS = {
    // When the student studies, Sun..Sat. Minutes after midnight; on:false = rest day.
    // Focus minutes = window length minus a breakMin rest after every maxBlock of work.
    win: [{ on: false, start: 600, end: 840 },  { on: true, start: 1020, end: 1260 }, { on: true, start: 1020, end: 1260 },
          { on: true, start: 1020, end: 1260 }, { on: true, start: 1020, end: 1260 }, { on: true, start: 1020, end: 1260 },
          { on: true, start: 540, end: 840 }],
    dayMax: 300,               // hard ceiling on focused minutes in one day (attention limit)
    breakMin: 10,              // rest after each work block
    hoursPerLecture: 1.5,      // total hours planned per lecture/lab covered (out-of-class)
    minHours: 6, maxHours: 24, // clamp on an exam's total
    startWeeks: 4,             // begin studying an exam this many weeks out (later if its lectures come later)
    practicalHours: 8,         // OSCE / practical exams, which cover no numbered lectures
    practicalLead: 21,         // days before a practical that practice begins
    retestHours: 8, retestLead: 14,
    firstPassShare: 0.30,      // share of a lecture's hours spent in its first days after delivery
    firstPassDays: 3,          // ...within this many days of delivery
    reviewGapPct: 0.20,        // gap between reviews = this fraction of the days left (Cepeda 2008)
    finalWeekShare: 0.35,      // share of the exam's total reserved for the last `finalDays` days
    finalDays: 7,
    rampPower: 1.6,            // >1 = back-loaded ramp, 1 = flat
    taperLastDayMin: 60,       // the day before an exam is light
    minBlock: 15, maxBlock: 50, // minutes per task
    planRetests: false,
    catchUpMax: 1.6            // most a missed backlog may inflate the remaining days
  };
  var PRESETS = {
    balanced:  { label: "Balanced",   note: "Steady keep-up after each lecture, then a heavier final week.", p: {} },
    keepup:    { label: "Keep-up",    note: "More work right after each lecture, lighter final week.",
                 p: { firstPassShare: 0.45, finalWeekShare: 0.25, rampPower: 1.2 } },
    latecrunch:{ label: "Late push",  note: "Light early, most hours in the last week (riskier).",
                 p: { firstPassShare: 0.15, finalWeekShare: 0.50, rampPower: 2.2 } },
    light:     { label: "Light",      note: "Fewer hours per lecture, about 17% less than Balanced.",
                 p: { hoursPerLecture: 1.25, minHours: 4 } }
  };
  function settingsWith(base, over) {
    var o = {}, k;
    for (k in DEFAULTS) o[k] = DEFAULTS[k];
    if (base) for (k in base) if (base[k] !== undefined) o[k] = base[k];
    if (over) for (k in over) if (over[k] !== undefined) o[k] = over[k];
    return o;
  }

  /* -------------------------------------------------- calendar -> exams -- */
  function classPrefix(t) { return String(t).replace(/\s*[-–]\s*(?:EXAM|RETEST|Course Remediation).*$/i, "").replace(/^RETEST:\s*/i, "").trim(); }

  function lectureNo(title) {
    var m = String(title).match(/(?:lecture|lec)\s*[-#:\s]*#?\s*(\d+)/i);
    return m ? +m[1] : null;
  }
  function labNo(title) {
    var m = String(title).match(/lab\s*[-#:\s]*#?\s*(\d+)/i);
    return m ? +m[1] : null;
  }

  /* "(Lectures 7-10 and Lab 2)" -> { lec:[7,8,9,10], lab:[2] } ; "(4-8)" -> lec 4..8 */
  function parseCoverage(title) {
    var m = String(title).match(/\(([^)]*)\)/);
    var out = { lec: [], lab: [] };
    if (!m) return out;
    var body = m[1].toLowerCase().replace(/&/g, " and ");
    body.split(/\band\b|,|;/).forEach(function (seg) {
      var isLab = /lab/.test(seg);
      var r = seg.match(/(\d+)\s*[-–]\s*(\d+)/);
      var one = seg.match(/(\d+)/);
      var list = isLab ? out.lab : out.lec;
      if (r) { for (var i = +r[1]; i <= +r[2]; i++) list.push(i); }
      else if (one) list.push(+one[1]);
    });
    return out;
  }

  function isGraded(kind, planRetests) {
    return kind === "exam" || (planRetests && (kind === "retest" || kind === "remediation"));
  }

  /* events: [{d,t,c,k,s}]. Returns exams on/after `from`, each with units and a
     release date per unit. */
  function deriveExams(events, from, cfg) {
    var lecDates = {}, labDates = {};
    events.forEach(function (e) {
      if (!e.c) return;
      if (e.k === "lecture") { var n = lectureNo(e.t); if (n != null) (lecDates[e.c] = lecDates[e.c] || {})[n] = e.d; }
      else if (e.k === "lab") { var l = labNo(e.t); if (l != null) (labDates[e.c] = labDates[e.c] || {})[l] = e.d; }
    });
    var out = [];
    events.forEach(function (e) {
      if (!isGraded(e.k, cfg.planRetests) || e.d < from || !e.c) return;
      var cov = parseCoverage(e.t), units = [];
      cov.lec.forEach(function (n) { units.push({ kind: "lec", n: n, date: (lecDates[e.c] || {})[n] || null }); });
      cov.lab.forEach(function (n) { units.push({ kind: "lab", n: n, date: (labDates[e.c] || {})[n] || null }); });
      var practical = !units.length, retest = e.k !== "exam";
      // A unit with no date on the calendar is released 3 weeks out at the latest.
      units.forEach(function (u) { if (!u.date || u.date >= e.d) u.date = add(e.d, -21); });
      units.sort(function (a, b) { return a.date < b.date ? -1 : a.date > b.date ? 1 : (a.n - b.n); });
      out.push({
        id: e.c + "|" + e.d + "|" + classPrefix(e.t) + "|" + (e.t.match(/#\s*(\d+)/) || [0, ""])[1] + (retest ? "|r" : ""),
        d: e.d, t: e.t, name: classPrefix(e.t) + (retest ? " (retest)" : ""), c: e.c, kind: e.k,
        units: units, practical: practical, retest: retest,
        num: (e.t.match(/(?:exam|#)\s*#?\s*(\d+)/i) || [0, null])[1] ? +(e.t.match(/(?:exam|#)\s*#?\s*(\d+)/i)[1]) : null,
        osce: /osce|practicum|practical/i.test(e.t)
      });
    });
    out.sort(function (a, b) { return a.d < b.d ? -1 : a.d > b.d ? 1 : 0; });
    return out;
  }

  /* ------------------------------------------------------------ demand -- */
  function examHours(x, cfg, ovr) {
    ovr = ovr || {};
    if (ovr.hours != null) return +ovr.hours;
    var base;
    if (x.retest) base = cfg.retestHours;
    else if (x.practical) base = cfg.practicalHours;
    else base = Math.max(cfg.minHours, Math.min(cfg.maxHours, cfg.hoursPerLecture * x.units.length));
    return base * (ovr.difficulty != null ? +ovr.difficulty : 1);
  }

  /* Minutes of study an exam needs, and WHEN each piece may happen.
       earliest  the first day the material exists (a lecture cannot be reviewed
                 before it is taught)
       ideal     the day this piece would ideally happen
       latest    the day before the exam
     Kinds: firstpass (right after delivery), review (spaced revisit), final
     (whole-exam practice in the last days). */
  function demandFor(x, cfg, ovr) {
    ovr = ovr || {};
    cfg = settingsWith(cfg, ovr.settings);
    var H = examHours(x, cfg, ovr) * 60;
    var D = x.d, last = add(D, -1), items = [];
    var finalStart = add(D, -cfg.finalDays);
    var units = x.units.slice();

    // Practicals and retests cover no numbered lectures: synthesise 4 practice
    // units spread over the lead-in so the same rules apply.
    if (!units.length) {
      var lead = x.retest ? cfg.retestLead : cfg.practicalLead;
      var span = Math.max(1, lead - cfg.finalDays);
      for (var i = 0; i < 4; i++) units.push({ kind: "prac", n: i + 1, date: add(D, -lead + Math.round(i * span / 4)) });
    }
    else {
      // Lectures delivered before the study window opens are not all studied on
      // one day: they are staggered across the first half of the lead-in.
      var startDay = ovr.start || add(D, -Math.round(cfg.startWeeks * 7));
      var early = units.filter(function (u) { return u.date < startDay; }), span = Math.max(0, Math.round((diff(startDay, D) - cfg.finalDays) * 0.5)), ei = 0;
      units = units.map(function (u) {
        if (u.date >= startDay) return u;
        var eff = add(startDay, Math.floor(ei++ * span / Math.max(1, early.length)));
        return { kind: u.kind, n: u.n, date: eff, delivered: u.date };
      });
    }
    var n = units.length;
    var finalPool = H * cfg.finalWeekShare;
    var per = (H - finalPool) / n;
    var lastRelease = units.reduce(function (m, u) { return u.date > m ? u.date : m; }, "0000-00-00");

    units.forEach(function (u, idx) {
      var late = u.date >= finalStart;                       // taught inside the final week
      var fp = late ? per : per * cfg.firstPassShare;
      items.push({ exam: x.id, kind: "firstpass", unit: u, minutes: fp, earliest: u.date,
                   ideal: add(u.date, 1) > last ? u.date : add(u.date, 1),
                   latest: late ? last : add(u.date, cfg.firstPassDays + 2) > last ? last : add(u.date, cfg.firstPassDays + 2) });
      if (late) return;
      var rest = per - fp, days = diff(u.date, finalStart);
      var gap = Math.max(2, Math.round(cfg.reviewGapPct * diff(u.date, D)));
      var ts = [];
      for (var t = add(u.date, 1 + gap); t < finalStart; t = add(t, gap)) ts.push(t);
      if (!ts.length) { finalPool += rest; return; }          // nothing fits before the final week
      var ws = ts.map(function (_, k) { return Math.pow(k + 1, Math.max(0, cfg.rampPower - 1)); });
      var sw = ws.reduce(function (a, b) { return a + b; }, 0);
      ts.forEach(function (day, k) {
        items.push({ exam: x.id, kind: "review", unit: u, minutes: rest * ws[k] / sw, earliest: add(day, -Math.floor(gap / 2)) < u.date ? u.date : add(day, -Math.floor(gap / 2)),
                     ideal: day, latest: add(day, Math.max(1, Math.floor(gap / 2))) >= finalStart ? add(finalStart, -1) : add(day, Math.max(1, Math.floor(gap / 2))) });
      });
    });

    // Final pool over the last days, but never before the last lecture exists.
    var fs = finalStart > add(lastRelease, 1) ? finalStart : add(lastRelease, 1);
    if (fs > last) fs = last;
    var fdays = range(fs, last), m = fdays.length;
    var fw = fdays.map(function (_, j) { var w = Math.pow(j + 1, cfg.rampPower); return j === m - 1 && m > 1 ? w * 0.4 : w; });
    var sfw = fw.reduce(function (a, b) { return a + b; }, 0);
    fdays.forEach(function (day, j) {
      var mins = finalPool * fw[j] / sfw;
      if (j === m - 1 && m > 1) mins = Math.min(mins, cfg.taperLastDayMin);
      items.push({ exam: x.id, kind: "final", unit: null, minutes: mins, earliest: fs, ideal: day, latest: last, daysOut: diff(day, D) });
    });
    return { items: items, hours: H / 60 };
  }

  /* --------------------------------------------------------- scheduling -- */
  /* Focused minutes a day can hold, from the student's own start/quit times.
     `nowMin` (today only) trims the window to what is still ahead. */
  function windowOf(day, cfg, nowMin, isToday) {
    var w = (cfg.win && cfg.win[dow(day)]) || { on: false, start: 0, end: 0 };
    if (!w.on) return null;
    var start = w.start, end = w.end;
    if (isToday && nowMin != null && nowMin > start) start = Math.ceil(nowMin / 5) * 5;
    if (end - start < 10) return null;
    return { start: start, end: end };
  }
  function capOf(win, cfg) {
    if (!win) return 0;
    var len = win.end - win.start, blk = Math.max(15, cfg.maxBlock) - 5, br = Math.max(0, cfg.breakMin);
    var focus = Math.floor(len * blk / (blk + br) / 5) * 5;
    return Math.max(0, Math.min(cfg.dayMax, focus));
  }
  function capacityFor(day, cfg, off, used, nowMin, today) {
    if (off && off[day]) return 0;
    var c = capOf(windowOf(day, cfg, nowMin, day === today), cfg);
    return Math.max(0, c - ((used && used[day]) || 0));
  }
  /* Lay a day's tasks on the clock inside the student's window (adds start/end). */
  function timeline(tasks, day, cfg, nowMin, today) {
    var w = windowOf(day, cfg, nowMin, day === today);
    if (!w) return tasks;
    var t = w.start, run = 0, blk = Math.max(15, cfg.maxBlock) - 5;
    // A rest follows every ~maxBlock minutes of accumulated work, not every task,
    // so several short tasks do not eat the window with breaks (capOf agrees).
    return tasks.map(function (k) {
      var o = Object.assign({}, k, { start: t, end: t + k.minutes });
      t += k.minutes; run += k.minutes;
      if (run >= blk) { t += cfg.breakMin; run = 0; }
      return o;
    });
  }

  /* exams: from deriveExams (already filtered). ovr: {examId:{hours,difficulty,off,settings}}.
     doneByExam: minutes already completed per exam (any day). usedByDay: minutes
     already committed on a day (today's frozen tasks). Returns
     { days: {ymd:[{exam, kind, unit, minutes, daysOut}]}, shortfall:{examId:min},
       demand:{examId:{hours,pending}} } */
  function plan(exams, today, cfg, ovr, doneByExam, offDays, usedByDay, nowMin, floor) {
    ovr = ovr || {}; doneByExam = doneByExam || {};
    var cap = {}, days = {}, shortfall = {}, info = {};
    var horizon = exams.reduce(function (m, x) { return x.d > m ? x.d : m; }, today);
    range(today, horizon).forEach(function (d) { cap[d] = capacityFor(d, cfg, offDays, usedByDay, nowMin, today); days[d] = []; });

    exams.filter(function (x) { return !(ovr[x.id] && ovr[x.id].off) && x.d > today; }).forEach(function (x) {
      var o = ovr[x.id] || {}, xc = settingsWith(cfg, o.settings);
      var dem = demandFor(x, xc, o);
      // Days before the student started using the planner are not held against them.
      var items = dem.items.filter(function (it) { return it.minutes > 0.5 && !(floor && !o.fresh && it.ideal < floor); })
        .sort(function (a, b) { return a.ideal < b.ideal ? -1 : a.ideal > b.ideal ? 1 : 0; });
      // Work already done consumes the oldest demand first; what is left is pending.
      var done = doneByExam[x.id] || 0, total = 0;
      items.forEach(function (it) { total += it.minutes; });
      var pending = [], consumed = done;
      items.forEach(function (it) {
        if (consumed >= it.minutes) { consumed -= it.minutes; return; }
        var left = it.minutes - consumed; consumed = 0;
        pending.push(Object.assign({}, it, { minutes: left }));
      });
      // Anything whose ideal day has passed becomes catch-up, due now.
      var behind = 0;
      pending.forEach(function (it) { if (it.ideal < today) { behind += it.minutes; it.ideal = today; if (it.earliest < today) it.earliest = today; } });
      pending.forEach(function (it) { if (it.earliest < today) it.earliest = today; });
      info[x.id] = { hours: dem.hours, totalMin: total, doneMin: done, pendingMin: pending.reduce(function (a, b) { return a + b.minutes; }, 0), behindMin: behind };
      x._pending = pending;
    });

    // Nearest exam first: it gets its ideal days; later exams flex around it.
    exams.filter(function (x) { return x._pending; }).sort(function (a, b) { return a.d < b.d ? -1 : a.d > b.d ? 1 : 0; })
      .forEach(function (x) {
        x._pending.sort(function (a, b) { return a.ideal < b.ideal ? -1 : a.ideal > b.ideal ? 1 : 0; }).forEach(function (it) {
          var m = Math.round(it.minutes / 5) * 5; if (m < 5) return;
          var lo = it.earliest < today ? today : it.earliest, hi = it.latest >= x.d ? add(x.d, -1) : it.latest;
          if (lo > hi) lo = hi;
          var cand = range(lo < today ? today : lo, hi < today ? today : hi).filter(function (d) { return cap[d] > 0; });
          cand.sort(function (a, b) {
            var da = Math.abs(diff(it.ideal, a)), db = Math.abs(diff(it.ideal, b));
            return da !== db ? da - db : (a < b ? -1 : 1);
          });
          var left = m;
          for (var i = 0; i < cand.length && left > 0; i++) {
            var d = cand[i], take = Math.min(cap[d], left);
            if (left - take > 0 && left - take < xc_min(cfg)) take = Math.min(cap[d], left);   // avoid crumbs
            if (take < 5) continue;
            cap[d] -= take; left -= take;
            days[d].push({ exam: x.id, kind: it.kind, unit: it.unit, minutes: take, daysOut: diff(d, x.d) });
          }
          if (left > 0) shortfall[x.id] = (shortfall[x.id] || 0) + left;
        });
        delete x._pending;
      });
    function xc_min(c) { return c.minBlock || 15; }
    // Fold tiny same-exam chunks on a day together so a day reads as a few tasks.
    Object.keys(days).forEach(function (d) { days[d] = timeline(tidyDay(days[d], cfg), d, cfg, nowMin, today); });
    return { days: days, shortfall: shortfall, info: info };
  }

  /* Merge a day's chunks: same exam+kind become one task (units listed), then
     split anything over maxBlock into sensible sessions. */
  function tidyDay(chunks, cfg) {
    var byKey = {}, order = [];
    chunks.forEach(function (c) {
      var k = c.exam + "|" + c.kind;
      if (!byKey[k]) { byKey[k] = { exam: c.exam, kind: c.kind, units: [], minutes: 0, daysOut: c.daysOut }; order.push(k); }
      var g = byKey[k]; g.minutes += c.minutes;
      if (c.unit && !g.units.some(function (u) { return u.kind === c.unit.kind && u.n === c.unit.n; })) g.units.push(c.unit);
    });
    var out = [];
    order.forEach(function (k) {
      var g = byKey[k], left = g.minutes, maxB = cfg.maxBlock, minB = cfg.minBlock;
      var parts = Math.max(1, Math.ceil(left / maxB)), each = Math.round(left / parts / 5) * 5;
      if (each < minB) { parts = 1; each = Math.round(left / 5) * 5; }
      for (var p = 0; p < parts; p++) {
        var mins = p === parts - 1 ? left : each;
        if (mins < 5) continue;
        out.push({ exam: g.exam, kind: g.kind, units: g.units, minutes: mins, daysOut: g.daysOut, part: parts > 1 ? (p + 1) + "/" + parts : "" });
        left -= mins;
      }
    });
    return out;
  }

  /* ----------------------------------------------------------- streaks -- */
  /* days: {ymd: {tasks:[{done, custom}], off:bool}}. A day is "planned" when it
     has at least one non-custom task and is not marked off. Replayed from the
     log every time, so editing an old day stays consistent.
       complete day  -> streak +1; every 5 complete days earns a freeze (max 2)
       missed day    -> a freeze is spent if one is banked, else the streak resets
       unplanned day -> neutral (rest days, days off, days nothing was due)  */
  function replayStreak(days, today, opts) {
    opts = opts || {};
    var maxFreezes = opts.maxFreezes || 2, every = opts.freezeEvery || 5;
    var keys = Object.keys(days).sort();
    var s = { streak: 0, best: 0, freezes: 0, complete: 0, progress: 0, every: every, frozen: [], broken: [], todayDone: false, todayPlanned: false };
    if (!keys.length) return s;
    var progress = 0;
    range(keys[0], today).forEach(function (d) {
      var rec = days[d];
      var real = rec && !rec.off ? (rec.tasks || []).filter(function (t) { return !t.custom; }) : [];
      var planned = real.length > 0, done = planned && real.every(function (t) { return t.done; });
      if (d === today) { s.todayPlanned = planned; s.todayDone = done; }
      if (!planned) return;
      if (done) {
        s.streak++; s.complete++; progress++;
        if (progress >= every) { progress = 0; if (s.freezes < maxFreezes) s.freezes++; }
        if (s.streak > s.best) s.best = s.streak;
      } else if (d < today) {
        if (s.freezes > 0) { s.freezes--; s.frozen.push(d); }
        else { if (s.streak > 0) s.broken.push({ d: d, streak: s.streak }); s.streak = 0; }
      }
    });
    s.progress = progress;
    return s;
  }

  /* -------------------------------------------------------------- stats -- */
  function doneMinutes(rec) {
    return (rec && rec.tasks ? rec.tasks : []).reduce(function (a, t) { return a + (t.done ? Math.max(t.minutes || 0, t.logged || 0) : (t.logged || 0)); }, 0);
  }
  function doneByExam(days) {
    var out = {};
    Object.keys(days).forEach(function (d) {
      (days[d].tasks || []).forEach(function (t) {
        if (!t.exam) return;
        out[t.exam] = (out[t.exam] || 0) + (t.done ? Math.max(t.minutes || 0, t.logged || 0) : (t.logged || 0));
      });
    });
    return out;
  }
  function weeklyMinutes(days, today, weeks) {
    var out = [], mon = mondayOf(today);
    for (var w = weeks - 1; w >= 0; w--) {
      var start = add(mon, -7 * w), tot = 0;
      range(start, add(start, 6)).forEach(function (d) { tot += doneMinutes(days[d]); });
      out.push({ start: start, minutes: tot });
    }
    return out;
  }
  /* Exams landing close together: windows of `span` days holding >= `min` graded dates. */
  function crunches(exams, span, min) {
    var out = [], i = 0;
    while (i < exams.length) {
      var j = i;
      while (j + 1 < exams.length && diff(exams[i].d, exams[j + 1].d) <= span) j++;
      if (j - i + 1 >= min) { out.push({ from: exams[i].d, to: exams[j].d, count: j - i + 1, ids: exams.slice(i, j + 1).map(function (e) { return e.id; }) }); i = j + 1; }
      else i++;
    }
    return out;
  }

  return {
    DEFAULTS: DEFAULTS, PRESETS: PRESETS, settingsWith: settingsWith,
    parse: parse, fmt: fmt, add: add, diff: diff, dow: dow, mondayOf: mondayOf, range: range,
    lectureNo: lectureNo, parseCoverage: parseCoverage, deriveExams: deriveExams,
    examHours: examHours, windowOf: windowOf, capOf: capOf, timeline: timeline, demandFor: demandFor, plan: plan, tidyDay: tidyDay,
    replayStreak: replayStreak, doneMinutes: doneMinutes, doneByExam: doneByExam,
    weeklyMinutes: weeklyMinutes, crunches: crunches
  };
});
