/* Homepage behaviour, extracted from index.html's inline <script> blocks.
   Concatenated in their original document order and loaded with `defer`
   placed BEFORE theme.js -- deferred scripts run in tag order after parsing,
   which reproduces the old ordering (inline body scripts completed before
   deferred theme.js ran). Safe to defer because every element they query is
   markup that already precedes them: the last quiz-link is at line 2679, the
   first of these blocks was at 2791.
   The two <script>s still inline in <head> stay there on purpose -- the theme
   setter must run before first paint to avoid a flash, and gtag defines
   window.dataLayer for the async tag. */

/* ---- from index.html (was inline at line 1407) ---- */
document.querySelectorAll(".semester").forEach(semester => {
      const semKey = "activeTab:" + semester.dataset.semester;
      semester.querySelectorAll(".tab-btn").forEach(btn => {
        btn.addEventListener("click", () => {
          semester.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
          semester.querySelectorAll(".tab-panel").forEach(p => p.classList.remove("active"));
          btn.classList.add("active");
          document.getElementById(btn.dataset.tab).classList.add("active");
          localStorage.setItem(semKey, btn.dataset.tab);
        });
      });
      const saved = localStorage.getItem(semKey);
      if (!saved) return;
      const btn = semester.querySelector(`.tab-btn[data-tab="${saved}"]`);
      if (!btn) return;
      semester.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
      semester.querySelectorAll(".tab-panel").forEach(p => p.classList.remove("active"));
      btn.classList.add("active");
      document.getElementById(saved).classList.add("active");
    });

    document.querySelectorAll("a.quiz-link").forEach(a => {
      try {
        const pathname = new URL(a.getAttribute("href"), location.href).pathname;
        const raw = localStorage.getItem("qc:" + pathname);
        if (!raw) return;
        const { score, total } = JSON.parse(raw);
        a.dataset.quizLabel = a.textContent.trim();
        const badge = document.createElement("span");
        badge.className = "score-badge";
        badge.textContent = `${score} / ${total}`;
        a.appendChild(badge);
      } catch (e) {}
    });

    (function () {
      /* Semester progress bar. Dates now come from semesters.js rather than
         hand-edited constants here, and the bar is rendered per .semester
         block, so a second semester needs no change to this code.

         The behaviours the old constants documented are preserved: `end` is
         the last REAL day (remediation exams happen on it, so the whole day
         still reads as in progress), `lastClassDay` is distinct from it
         because the final exam week is not class days, and totalWeeks is the
         program's own count rather than derived from the span. */
      var reg = window.Semesters;
      if (!reg) return;

      document.querySelectorAll(".semester").forEach(function (block) {
        var sem = reg.byId(block.dataset.semester);
        var fill = block.querySelector(".semester-progress-fill, #semester-progress-fill");
        var label = block.querySelector(".semester-progress-label, #semester-progress-label");
        if (!sem || !fill || !label) return;

        var start = reg.startOf(sem);
        var end = reg.endOf(sem);
        var lastClass = reg.parseLocal(sem.lastClassDay, true);
        var now = new Date();
        var elapsedMs = now - start;
        var pct = Math.max(0, Math.min(100, (elapsedMs / (end - start)) * 100));
        var dayMs = 24 * 60 * 60 * 1000;
        var weekNum = Math.max(1, Math.min(sem.totalWeeks,
                        Math.floor(elapsedMs / (7 * dayMs)) + 1));

        // weekdays strictly AFTER today through the last class day, so today
        // is never counted among the days still remaining
        function countWeekdaysLeft(fromExclusive, toInclusive) {
          var count = 0;
          var d = new Date(fromExclusive.getFullYear(), fromExclusive.getMonth(),
                           fromExclusive.getDate() + 1);
          var stop = new Date(toInclusive.getFullYear(), toInclusive.getMonth(),
                              toInclusive.getDate());
          while (d <= stop) {
            var dow = d.getDay();
            if (dow !== 0 && dow !== 6) count++;
            d.setDate(d.getDate() + 1);
          }
          return count;
        }
        var classDaysLeft = countWeekdaysLeft(now, lastClass);

        requestAnimationFrame(function () { fill.style.width = pct + "%"; });
        if (now < start) {
          // "starts soon" was fine when the only future term was weeks away;
          // with the whole didactic year listed, say WHEN -- and don't state an
          // estimated date as though it were on a syllabus
          var when = start.toLocaleDateString(undefined, { month: "long", day: "numeric", year: "numeric" });
          label.textContent = sem.estimated
            ? "Starts around " + when + " · dates to be confirmed"
            : "Starts " + when;
        } else if (now > end) {
          label.textContent = "Semester complete!";
        } else {
          label.textContent = "Week " + weekNum + " of " + sem.totalWeeks + " \u00b7 " +
            classDaysLeft + " class day" + (classDaysLeft === 1 ? "" : "s") + " left";
        }
      });
    })();

    (function () {
      /* Semester countdown: first day of class through the last exam on the
         calendar. It answers the one question the progress bar above does not
         -- "how much longer is this" -- in whole days rather than weeks.

         The target is the LAST GRADED DATE in calendar-data.js, not the
         semester's `end`. They happen to be the same day for Fall 2026, but
         `end` is a hand-set boundary while the graded list is generated from
         the school's own PDFs, so keying off the data means a rescheduled
         final moves the countdown without anyone editing the registry.

         Rendered per .semester block from the same markup, so Spring and
         Summer II get it for free once their calendars land. */
      var reg = window.Semesters;
      var cal = window.CalendarData;
      if (!reg) return;

      var DAY = 24 * 60 * 60 * 1000;
      function midnight(d) { return new Date(d.getFullYear(), d.getMonth(), d.getDate()); }
      function daysBetween(a, b) { return Math.round((midnight(b) - midnight(a)) / DAY); }
      function longDate(d) {
        return d.toLocaleDateString("en-US",
          { weekday: "long", month: "long", day: "numeric" });
      }

      document.querySelectorAll(".semester").forEach(function (block) {
        var el = block.querySelector(".semester-countdown");
        var sem = reg.byId(block.dataset.semester);
        if (!el || !sem) return;

        var now = new Date();
        var start = reg.startOf(sem);

        // last graded date for this term, else fall back to the registry's end
        var lastEvent = null;
        if (cal) {
          cal.forSemester(sem.id).forEach(function (e) {
            if (cal.isGraded(e) && (!lastEvent || e.d > lastEvent.d)) lastEvent = e;
          });
        }
        var target = lastEvent ? reg.parseLocal(lastEvent.d) : reg.endOf(sem);

        var toStart = daysBetween(now, start);
        var toEnd = daysBetween(now, target);

        /* Retire the countdown only once the last exam is genuinely PAST.
           Comparing `now > target` instead hid it from midnight on the morning
           of the final exam -- target is local midnight, so every hour of the
           day it counts down to compares as later than it. */
        if (toEnd < 0) return;

        /* One shape for every term, whichever side of it you are standing on:
           a number, what the number counts, then "Day X of N" and the date it
           refers to. Before the term starts the number counts to the first day;
           once it has started, to the last exam. Holding the detail line to the
           same shape is the point -- four cards each phrasing this their own way
           read as four unrelated widgets rather than one. */
        var span = daysBetween(start, target) + 1;
        var num, main, sub;

        if (toStart > 0) {
          num = toStart;
          main = "day" + (toStart === 1 ? "" : "s") + " until classes start";
          sub = "Day 0 of " + span + " · " + longDate(start);
        } else {
          num = toEnd;
          main = toEnd === 0
            ? "the last exam is today"
            : "day" + (toEnd === 1 ? "" : "s") + " until the last exam";
          sub = "Day " + (daysBetween(start, now) + 1) + " of " + span + " · " +
                longDate(target) + (lastEvent ? " · " + lastEvent.t : "");
        }

        /* A term whose dates are still guesses gets the same countdown rather
           than none at all, but the number is marked approximate and the detail
           line says so. Printing "Day 0 of 116" off an invented start date would
           state a guess as fact, which is the one thing the estimated flag
           exists to prevent. */
        if (sem.estimated) {
          num = "~" + num;
          sub = "dates to be confirmed";
        }

        el.innerHTML = "";
        var n = document.createElement("div");
        n.className = "cd-num";
        n.textContent = String(num);
        var text = document.createElement("div");
        text.className = "cd-text";
        var m = document.createElement("div");
        m.className = "cd-main";
        m.textContent = main;
        var s = document.createElement("div");
        s.className = "cd-sub";
        s.textContent = sub;
        text.appendChild(m);
        text.appendChild(s);
        el.appendChild(n);
        el.appendChild(text);
        el.hidden = false;
      });
    })();

    (function () {
      /* Every graded date in the didactic year -- exams, retests and course
         remediation -- read from calendar-data.js rather than retyped here.
         This list used to be a hand-maintained array, and it silently went
         stale when the school moved three August dates; see calendar-data.js
         for that story. Regenerate with tools/gen_calendar_data.py. */
      const EXAM_EVENTS = (window.CalendarData ? window.CalendarData.graded() : [])
        .map(e => ({ date: e.d, title: e.t }));

      function displayWeekMonday(now) {
        const day = now.getDay(); // 0 Sun .. 6 Sat
        const diffToMonday = day === 0 ? -6 : 1 - day;
        const monday = new Date(now.getFullYear(), now.getMonth(), now.getDate() + diffToMonday);
        const afterFridayCutoff = day === 0 || day === 6 || (day === 5 && now.getHours() >= 17);
        if (afterFridayCutoff) monday.setDate(monday.getDate() + 7);
        return monday;
      }

      function ymd(d) {
        return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");
      }

      const monday = displayWeekMonday(new Date());
      const weekDates = [0, 1, 2, 3, 4].map(n => {
        const d = new Date(monday);
        d.setDate(monday.getDate() + n);
        return d;
      });
      const weekKeys = weekDates.map(ymd);
      const dayLabels = ["Mon", "Tue", "Wed", "Thu", "Fri"];

      // One-time exception: a handful of retest dates this semester landed on a
      // Saturday (the school's own scheduling, not something we'd move) -- rather
      // than redesigning the widget to always show weekends, only pull in Sat/Sun
      // for THIS specific displayed week if an actual event is scheduled that day.
      [5, 6].forEach(n => {
        const d = new Date(monday);
        d.setDate(monday.getDate() + n);
        const key = ymd(d);
        if (EXAM_EVENTS.some(e => e.date === key)) {
          weekDates.push(d);
          weekKeys.push(key);
          dayLabels.push(n === 5 ? "Sat" : "Sun");
        }
      });

      const fmt = d => d.toLocaleDateString("en-US", { month: "short", day: "numeric" });

      document.getElementById("week-range").textContent = fmt(weekDates[0]) + " – " + fmt(weekDates[weekDates.length - 1]);

      // Keep both floating sidebars (this one and #continue-widget) level with the
      // top of the semester card rather than the top of the page -- measured, not
      // hardcoded, so it stays correct if the header/subtitle text ever changes length.
      function alignSidebars() {
        const page = document.querySelector(".page");
        const card = document.getElementById("semester-card");
        if (!page || !card) return;
        // getBoundingClientRect() returns real (already-zoomed) viewport pixels,
        // but week-widget/continue-widget are descendants of .page -- when the
        // "Larger text" setting applies zoom to .page, any top:Npx set on them
        // gets re-scaled by that same zoom at render time. Divide out the
        // current zoom factor so the assigned value lands in the right spot
        // instead of being pushed down by an extra ~15%.
        const zoom = parseFloat(getComputedStyle(page).zoom) || 1;
        const offset = Math.round((card.getBoundingClientRect().top - page.getBoundingClientRect().top) / zoom);
        const weekEl = document.getElementById("week-widget");
        const continueEl = document.getElementById("continue-widget");
        const statsEl = document.getElementById("stats-widget");
        if (weekEl) weekEl.style.top = offset + "px";
        const relaxEl = document.getElementById("relax-cta-row");
        const groupEl = document.getElementById("group-cta-row");
        const arcadeEl = document.getElementById("arcade-cta-row");
        const guidesFloatBtn = document.getElementById("guides-btn-floating");
        const searchInput = document.getElementById("site-search");
        const searchWrap = document.querySelector(".search-wrap");
        // Top-of-rail line, aligned with the search-input row (above the stats card).
        let btnTop = offset;
        if (searchInput && searchWrap) {
          const searchHeight = searchInput.getBoundingClientRect().height / zoom;
          const gap = (card.getBoundingClientRect().top - searchWrap.getBoundingClientRect().bottom) / zoom;
          btnTop = Math.round(offset - searchHeight - gap);
          if (guidesFloatBtn) {
            guidesFloatBtn.style.height = Math.round(searchHeight) + "px";
            guidesFloatBtn.style.top = btnTop + "px";
          }
        }
        /* Left rail (top -> bottom): report-a-question pill -> Relax -> Group
           Study -> Arcade -> stats card -> Continue.

           The two rails mirror each other, which is what makes them read as one
           frame around the semester card rather than two lists that happen to
           sit beside it. The pill takes the search-input line (btnTop) opposite
           the Guides button; Relax then starts at `offset`, level with the top
           of the semester card, opposite the week widget. Relax used to hang
           off the bottom of the pill instead, which left the left rail starting
           a few pixels higher than the right and everything below it out of
           step.

           Each link below measures the one above, so inserting a widget means
           adding a link to this chain -- CSS alone leaves it stacked on
           whatever was there before. */
        var issueEl = document.getElementById("question-issue-row");
        if (issueEl) issueEl.style.top = btnTop + "px";
        if (relaxEl) relaxEl.style.top = offset + "px";
        var relaxH = relaxEl ? relaxEl.getBoundingClientRect().height / zoom : 0;
        var groupTop = offset + (relaxH ? relaxH + 18 : 0);
        if (groupEl) groupEl.style.top = groupTop + "px";
        var groupH = groupEl ? groupEl.getBoundingClientRect().height / zoom : 0;
        var arcadeTop = groupTop + (groupH ? groupH + 18 : 0);
        if (arcadeEl) arcadeEl.style.top = arcadeTop + "px";
        var arcadeH = arcadeEl ? arcadeEl.getBoundingClientRect().height / zoom : 0;
        var statsTop = arcadeTop + (arcadeH ? arcadeH + 18 : 0);
        if (statsEl) statsEl.style.top = statsTop + "px";
        var statsH = statsEl ? statsEl.getBoundingClientRect().height / zoom : 0;
        if (continueEl) continueEl.style.top = (statsTop + (statsH ? statsH + 18 : 0)) + "px";
      }
      alignSidebars();
      window.addEventListener("resize", alignSidebars);
      window.addEventListener("load", alignSidebars);

      const items = EXAM_EVENTS.filter(e => weekKeys.includes(e.date))
        .sort((a, b) => a.date.localeCompare(b.date));

      const listEl = document.getElementById("week-list");
      if (items.length === 0) {
        const empty = document.createElement("div");
        empty.className = "week-empty";
        empty.textContent = "Nothing scheduled this week.";
        listEl.appendChild(empty);
      } else {
        const todayKey = ymd(new Date());
        items.forEach(e => {
          const row = document.createElement("div");
          row.className = "week-item" + (e.date <= todayKey ? " done" : "");
          const dayIdx = weekKeys.indexOf(e.date);
          const day = document.createElement("span");
          day.className = "week-day";
          day.textContent = dayLabels[dayIdx];
          const title = document.createElement("span");
          title.className = "week-item-title";
          title.textContent = e.title;
          row.appendChild(day);
          row.appendChild(title);
          listEl.appendChild(row);
        });
      }
    })();

    (function () {
      const widget = document.getElementById("continue-widget");
      const list = document.getElementById("continue-list");
      // cloud-sync.js already timestamps every localStorage write (for its
      // own cross-device merge logic) in this same-origin meta map -- reuse
      // it here instead of relying on document order (which reflects
      // wherever a quiz link happens to sit on the page, not when it was
      // actually last played) so "most recent" is actually accurate.
      let lastWriteMeta = {};
      try { lastWriteMeta = JSON.parse(localStorage.getItem("__cloudSyncMeta")) || {}; } catch (e) {}
      const entries = [];
      document.querySelectorAll("a.quiz-link").forEach(a => {
        try {
          const pathname = new URL(a.getAttribute("href"), location.href).pathname;
          const pkey = "qp:" + pathname;
          const raw = localStorage.getItem(pkey);
          if (!raw) return;
          const saved = JSON.parse(raw);
          const current = saved.current ?? saved.i ?? saved.idx;
          if (current === undefined) return;
          const total = saved.total ?? (saved.order ? saved.order.length : undefined);
          entries.push({
            href: a.getAttribute("href"),
            lastWriteMs: lastWriteMeta[pkey] || 0,
            label: a.dataset.quizLabel || a.textContent.trim(),
            current, total,
            score: saved.score
          });
        } catch (e) {}
      });
      if (entries.length === 0) return;
      entries.sort((a, b) => b.lastWriteMs - a.lastWriteMs);
      entries.slice(0, 5).forEach(entry => {
        const item = document.createElement("a");
        item.className = "continue-item";
        item.href = entry.href;

        const top = document.createElement("div");
        top.className = "ci-top";
        const title = document.createElement("span");
        title.className = "ci-title";
        title.textContent = entry.label;
        const meta = document.createElement("span");
        meta.className = "ci-meta";
        meta.textContent = entry.total
          ? `Question ${entry.current + 1} of ${entry.total} · Score ${entry.score}`
          : `Question ${entry.current + 1} · Score ${entry.score}`;
        top.appendChild(title);
        top.appendChild(meta);
        item.appendChild(top);

        if (entry.total) {
          const bar = document.createElement("div");
          bar.className = "ci-bar";
          const fill = document.createElement("i");
          fill.style.width = Math.round((entry.current / entry.total) * 100) + "%";
          bar.appendChild(fill);
          item.appendChild(bar);
        }
        list.appendChild(item);
      });
      widget.classList.remove("hidden");

      function alignWidgetToCard() {
        const page = document.querySelector(".page");
        const card = document.querySelector(".card");
        if (!page || !card) return;
        const top = card.getBoundingClientRect().top - page.getBoundingClientRect().top;
        widget.style.top = top + "px";
      }
      alignWidgetToCard();
      window.addEventListener("resize", alignWidgetToCard);
    })();

    document.querySelectorAll(".exam-section, .topic-section").forEach(section => {
      const key = "examOpen:" + section.dataset.examid;
      const saved = localStorage.getItem(key);
      if (saved !== null) section.open = saved === "true";
      section.addEventListener("toggle", () => {
        localStorage.setItem(key, section.open);
      });
    });


    (function () {
      /* Semester switcher. The card's own heading IS the control -- clicking
         "Summer Semester 1 - 2026" opens a menu of the terms, and switching
         swaps the whole card (tabs, quizzes, progress bar) underneath it. A
         separate row of pills above the heading said the same thing twice.

         The menu itself is semester-picker.js, shared with the guides page and
         the Arcade. Only semesters that actually have a .semester block are
         offered, and with one the heading stays plain text. Selection persists
         and defaults to whichever semester today falls in. */
      var reg = window.Semesters;
      if (!reg || !window.SemesterPicker) return;

      var blocks = {};
      document.querySelectorAll(".semester").forEach(function (b) {
        if (b.dataset.semester) blocks[b.dataset.semester] = b;
      });
      var present = reg.all.filter(function (sem) { return blocks[sem.id]; });
      window.__semesterBlocks = blocks;

      var pickers = [];

      function show(id) {
        Object.keys(blocks).forEach(function (k) {
          blocks[k].classList.toggle("hidden", k !== id);
        });
        // every block carries its own picker; keep them all in step so the
        // heading is right whichever block you land on
        pickers.forEach(function (p) { p.setActive(id); });
        window.__activeSemester = id;
        try { localStorage.setItem("activeSemester", id); } catch (e) {}
        // search results are scoped to the visible semester, so re-run them
        var input = document.getElementById("site-search");
        if (input && input.value.trim() && window.__runSearch) window.__runSearch(input.value);
      }
      window.__showSemester = show;

      var saved = null;
      try { saved = localStorage.getItem("activeSemester"); } catch (e) {}

      // Which term to open on -- the rule lives in the registry, because the
      // guides page and the Arcade share this same saved key and have to agree.
      var initial = reg.preferred(saved);
      if (!blocks[initial]) initial = reg.current().id;
      if (!blocks[initial]) initial = present.length ? present[0].id : null;

      if (present.length < 2) {
        // Single semester: no menu, but the heading still has to say something
        // -- it is empty in the markup precisely so this is the only place the
        // label comes from. Still record which one is active so search scoping
        // has an answer.
        var only = reg.byId(initial);
        var lone = only && blocks[initial] && blocks[initial].querySelector(".semester-header");
        if (lone) lone.textContent = only.label;
        window.__activeSemester = initial;
        return;
      }

      present.forEach(function (sem) {
        var header = blocks[sem.id].querySelector(".semester-header");
        if (!header) return;
        var picker = window.SemesterPicker({
          semesters: present, activeId: initial, onPick: show
        });
        if (!picker) return;
        header.textContent = "";
        header.appendChild(picker.el);
        pickers.push(picker);
      });

      show(initial);
    })();

    (function () {
      const input = document.getElementById("site-search");
      const resultsBox = document.getElementById("search-results");
      const tabLabels = {};
      document.querySelectorAll(".tab-btn").forEach(btn => {
        tabLabels[btn.dataset.tab] = btn.textContent.trim();
      });

      function breadcrumbFor(a) {
        const parts = [];
        let d = a.closest("details");
        while (d) {
          const label = d.querySelector(":scope > summary > span");
          if (label) parts.unshift(label.textContent.trim());
          d = d.parentElement ? d.parentElement.closest("details") : null;
        }
        const panel = a.closest(".tab-panel");
        const tabLabel = panel ? (tabLabels[panel.dataset.class] || "") : "";
        const href = a.getAttribute("href") || "";
        const kind = /\.pdf(?:$|[?#])/i.test(href) ? "PDF"
                   : /-study\.html(?:$|[?#])/i.test(href) ? "Study" : "Quiz";
        return [tabLabel, ...parts].filter(Boolean).join(" › ") + " · " + kind;
      }

      function runSearch(query) {
        const q = query.trim().toLowerCase();
        if (!q) {
          resultsBox.classList.add("hidden");
          resultsBox.innerHTML = "";
          return;
        }
        const links = Array.from(document.querySelectorAll("a.quiz-link"));
        const hit = a => (a.dataset.quizLabel || a.textContent).trim().toLowerCase().includes(q);
        // Results are scoped to the semester you are looking at. Exams are
        // cumulative and board prep reaches back, so a hit in the other
        // semester is offered rather than silently dropped.
        const semOf = a => {
          const block = a.closest("[data-semester]");
          return block ? block.getAttribute("data-semester") : null;
        };
        const active = window.__activeSemester || null;
        const all = links.filter(hit);
        const matches = (active ? all.filter(a => semOf(a) === active) : all).slice(0, 40);
        const elsewhere = active ? all.filter(a => semOf(a) !== active) : [];

        resultsBox.innerHTML = "";
        if (matches.length === 0 && elsewhere.length === 0) {
          const empty = document.createElement("div");
          empty.className = "search-no-results";
          empty.textContent = "No quizzes match “" + query.trim() + "”";
          resultsBox.appendChild(empty);
        } else if (matches.length === 0) {
          const none = document.createElement("div");
          none.className = "search-no-results";
          none.textContent = "Nothing in this semester matches “" + query.trim() + "”";
          resultsBox.appendChild(none);
        } else {
          matches.forEach((a, i) => {
            const label = (a.dataset.quizLabel || a.textContent).trim();
            const r = document.createElement("a");
            r.className = "search-result";
            r.href = a.getAttribute("href");
            if (i === 0) r.classList.add("active-result");
            const title = document.createElement("div");
            title.className = "sr-title";
            title.textContent = label;
            const path = document.createElement("div");
            path.className = "sr-path";
            path.textContent = breadcrumbFor(a);
            r.appendChild(title);
            r.appendChild(path);
            resultsBox.appendChild(r);
          });
        }

        // One line out to the other semester, so a scoped search is never a
        // dead end for material you genuinely have.
        if (elsewhere.length) {
          const reg = window.Semesters;
          const otherId = elsewhere[0].closest("[data-semester]").getAttribute("data-semester");
          const other = reg && reg.byId(otherId);
          const jump = document.createElement("button");
          jump.type = "button";
          jump.className = "search-other-sem";
          jump.textContent = elsewhere.length + " more in " +
            ((other && (other.short || other.label)) || "another semester") + " \u2192";
          jump.addEventListener("mousedown", e => e.preventDefault());
          jump.addEventListener("click", () => {
            if (window.__showSemester) window.__showSemester(otherId);
          });
          resultsBox.appendChild(jump);
        }
        resultsBox.classList.remove("hidden");
      }

      // Exposed so switching semesters can re-scope results that are already
      // on screen -- without this the "N more in Semester 1 →" jump changes the
      // semester but leaves the old "nothing matches" list sitting there.
      window.__runSearch = runSearch;

      input.addEventListener("input", () => runSearch(input.value));
      input.addEventListener("focus", () => { if (input.value.trim()) runSearch(input.value); });

      input.addEventListener("keydown", (e) => {
        if (e.key === "Escape") {
          input.value = "";
          resultsBox.classList.add("hidden");
          resultsBox.innerHTML = "";
          input.blur();
        } else if (e.key === "Enter") {
          const first = resultsBox.querySelector(".search-result");
          if (first) { e.preventDefault(); location.href = first.getAttribute("href"); }
        }
      });

      document.addEventListener("click", (e) => {
        if (!e.target.closest(".search-wrap")) {
          resultsBox.classList.add("hidden");
        }
      });
    })();

    (function () {
      const indicator = document.getElementById("pull-refresh");
      const path = indicator.querySelector("path");
      const pathLength = 420;
      const threshold = 70;
      const maxPull = 90;
      let startY = 0;
      let pulling = false;
      let refreshing = false;

      document.addEventListener("touchstart", (e) => {
        if (window.scrollY === 0 && !refreshing) {
          startY = e.touches[0].clientY;
          pulling = true;
        }
      }, { passive: true });

      document.addEventListener("touchmove", (e) => {
        if (!pulling || refreshing) return;
        const delta = e.touches[0].clientY - startY;
        if (delta > 0) {
          const dist = Math.min(delta * 0.5, maxPull);
          indicator.style.height = dist + "px";
          const progress = Math.min(dist / threshold, 1);
          path.style.strokeDashoffset = pathLength * (1 - progress);
        }
      }, { passive: true });

      document.addEventListener("touchend", () => {
        if (!pulling || refreshing) return;
        pulling = false;
        const currentHeight = parseInt(indicator.style.height || "0", 10);
        if (currentHeight >= threshold * 0.5) {
          refreshing = true;
          indicator.style.height = maxPull + "px";
          indicator.classList.add("refreshing");
          setTimeout(() => location.reload(), 500);
        } else {
          indicator.style.height = "0px";
          path.style.strokeDashoffset = pathLength;
        }
      });
    })();

/* ---- from index.html (was inline at line 1897) ---- */
(function () {
      const overlay = document.getElementById("review-modal-overlay");
      const content = document.getElementById("review-modal-content");
      const title = document.getElementById("review-modal-title");
      function openReview(quizName, reviewHTML) {
        title.textContent = quizName;
        content.innerHTML = reviewHTML;
        overlay.classList.add("open");
      }
      function closeReview() { overlay.classList.remove("open"); }
      document.getElementById("review-modal-close").addEventListener("click", closeReview);
      overlay.addEventListener("click", (e) => { if (e.target === overlay) closeReview(); });
      document.addEventListener("keydown", (e) => { if (e.key === "Escape") closeReview(); });

      document.querySelectorAll("a.quiz-link").forEach(a => {
        try {
          const pathname = new URL(a.getAttribute("href"), location.href).pathname;
          const raw = localStorage.getItem("qc:" + pathname);
          if (!raw) return;
          const saved = JSON.parse(raw);
          const badge = a.querySelector(".score-badge");
          if (!badge) return;
          badge.title = "Click to view your review";
          badge.addEventListener("click", (e) => {
            e.preventDefault();
            e.stopPropagation();
            const label = a.dataset.quizLabel || a.textContent.trim();
            if (saved.reviewHTML) {
              openReview(label, saved.reviewHTML);
            } else {
              openReview(label, '<p style="color:var(--muted)">No saved review from this attempt yet &mdash; finish this quiz once more to enable this.</p>');
            }
          });
        } catch (e) {}
      });
    })();

/* ---- from index.html (was inline at line 1936) ---- */
(function () {
      const overlay = document.getElementById("request-modal-overlay");
      const textarea = document.getElementById("request-text");
      function openModal() {
        overlay.classList.add("open");
        setTimeout(() => textarea.focus(), 0);
      }
      function closeModal() { overlay.classList.remove("open"); }
      document.getElementById("request-open").addEventListener("click", openModal);
      document.getElementById("request-modal-close").addEventListener("click", closeModal);
      document.getElementById("request-cancel").addEventListener("click", closeModal);
      overlay.addEventListener("click", (e) => { if (e.target === overlay) closeModal(); });
      document.addEventListener("keydown", (e) => { if (e.key === "Escape" && overlay.classList.contains("open")) closeModal(); });

      document.getElementById("request-send").addEventListener("click", () => {
        const message = textarea.value.trim();
        if (!message) { textarea.focus(); return; }
        const btn = document.getElementById("request-send");
        btn.disabled = true; btn.textContent = "Sending…";
        fetch("https://formspree.io/f/xdaqleod", {
          method: "POST",
          headers: { "Content-Type": "application/json", "Accept": "application/json" },
          body: JSON.stringify({ message: message, _subject: "PA Quizzes Feature/Exam Request", page: location.href })
        }).then((r) => {
          if (!r.ok) throw new Error("bad");
          closeModal(); showToast("Thanks! Your request was sent.");
        }).catch(() => {
          showToast("Could not send — please email jaxonluke22913@gmail.com.");
        }).finally(() => { btn.disabled = false; btn.textContent = "Send request"; });
      });
    })();

/* ---- from index.html (was inline at line 1970) ---- */
(function () {
      // Curated, not auto-generated from every recent commit -- only quizzes
      // meant to be highlighted to visitors as freshly added get an entry.
      // Update this list (and the "What's New" panel below) whenever new
      // quiz content ships. NEW_BADGE_DAYS controls how long a badge lasts.
      var NEW_QUIZZES = {
        "CAM%20Nutrition%20Exam%202/acupuncture-quiz.html": "2026-08-01",
        "CAM%20Nutrition%20Exam%202/acupuncture-quiz-version-2.html": "2026-08-01",
        "CAM%20Nutrition%20Exam%202/chiropractic-massage-homeopathy-quiz.html": "2026-08-01",
        "CAM%20Nutrition%20Exam%202/chiropractic-massage-homeopathy-quiz-version-2.html": "2026-08-01",
        "CAM%20Nutrition%20Exam%202/cam-nutrition-exam2-master-exam-form-a.html": "2026-08-01",
        "CAM%20Nutrition%20Exam%202/cam-nutrition-exam2-master-exam-form-b.html": "2026-08-01",
        "CAM%20Nutrition%20Exam%202/cam-nutrition-exam2-master-exam-form-c.html": "2026-08-01",
        "CAM%20Nutrition%20Exam%202/cam-nutrition-exam2-master-exam-form-d.html": "2026-08-01",
        "CAM%20Nutrition%20Exam%202/cam-nutrition-exam2-master-exam-form-e.html": "2026-08-01",
        "Physical%20Diagnosis%201%20Exam%203/soap-case-presentations-quiz.html": "2026-08-01",
        "Physical%20Diagnosis%201%20Exam%203/soap-case-presentations-quiz-version-2.html": "2026-08-01",
        "Physical%20Diagnosis%201%20Exam%203/pd1-exam3-master-exam-form-a.html": "2026-08-01",
        "Physical%20Diagnosis%201%20Exam%203/pd1-exam3-master-exam-form-b.html": "2026-08-01",
        "Physical%20Diagnosis%201%20Exam%203/pd1-exam3-master-exam-form-c.html": "2026-08-01",
        "Physical%20Diagnosis%201%20Exam%203/pd1-exam3-master-exam-form-d.html": "2026-08-01",
        "Physical%20Diagnosis%201%20Exam%203/pd1-exam3-master-exam-form-e.html": "2026-08-01",
        "CAM%20Nutrition%20Exam%202/herbal-medicines-medical-marijuana-quiz.html": "2026-07-29",
        "CAM%20Nutrition%20Exam%202/herbal-medicines-medical-marijuana-quiz-version-2.html": "2026-07-29",
        "CAM%20Nutrition%20Exam%202/animal-assisted-therapy-quiz.html": "2026-07-29",
        "CAM%20Nutrition%20Exam%202/animal-assisted-therapy-quiz-version-2.html": "2026-07-29",
        "Physical%20Diagnosis%201%20Exam%203/history-physical-documentation-quiz.html": "2026-07-28",
        "Physical%20Diagnosis%201%20Exam%203/history-physical-documentation-quiz-version-2.html": "2026-07-28",
        "CAM%20Nutrition%20Exam%202/introduction-to-cam-quiz.html": "2026-07-27",
        "CAM%20Nutrition%20Exam%202/introduction-to-cam-quiz-version-2.html": "2026-07-27",
        "Anatomy%20Exam%204/prof-shah-style-quiz.html": "2026-07-23",
        "Anatomy%20Exam%204/prof-shah-style-quiz-version-2.html": "2026-07-23",
        "Anatomy%20Exam%204/prof-shah-style-quiz-version-3.html": "2026-07-23",
        "Anatomy%20Exam%204/prof-shah-style-quiz-version-4.html": "2026-07-23",
        "Anatomy%20Exam%204/muscle-oian-quiz.html": "2026-07-23",
        "Anatomy%20Exam%204/muscle-oian-quiz-version-2.html": "2026-07-23",
        "Physiology%20Exam%204/bone-muscle-physiology-1-quiz.html": "2026-07-21",
        "Physiology%20Exam%204/bone-muscle-physiology-2-quiz.html": "2026-07-21",
        "Physiology%20Exam%204/physiology-master-exam-form-a.html": "2026-07-21",
        "Physiology%20Exam%204/physiology-master-exam-form-b.html": "2026-07-21",
        "Physiology%20Exam%204/physiology-master-exam-form-c.html": "2026-07-21",
        "Physiology%20Exam%204/physiology-master-exam-form-d.html": "2026-07-21",
        "Physiology%20Exam%204/physiology-master-exam-form-e.html": "2026-07-21",
        "CAM%20Nutrition%20Exam%201/pregnancy-breastfeeding-quiz.html": "2026-07-20",
        "CAM%20Nutrition%20Exam%201/pregnancy-breastfeeding-quiz-version-2.html": "2026-07-20",
        "CAM%20Nutrition%20Exam%201/food-allergies-intolerances-quiz.html": "2026-07-20",
        "CAM%20Nutrition%20Exam%201/food-allergies-intolerances-quiz-version-2.html": "2026-07-20",
        "CAM%20Nutrition%20Exam%201/nutrition-aging-quiz.html": "2026-07-25",
        "CAM%20Nutrition%20Exam%201/nutrition-aging-quiz-version-2.html": "2026-07-25",
        "CAM%20Nutrition%20Exam%201/infancy-adolescence-nutrition-quiz.html": "2026-07-25",
        "CAM%20Nutrition%20Exam%201/infancy-adolescence-nutrition-quiz-version-2.html": "2026-07-25",
        "CAM%20Nutrition%20Exam%201/cam-nutrition-master-exam-form-a.html": "2026-07-25",
        "CAM%20Nutrition%20Exam%201/cam-nutrition-master-exam-form-b.html": "2026-07-25",
        "CAM%20Nutrition%20Exam%201/cam-nutrition-master-exam-form-c.html": "2026-07-25",
        "CAM%20Nutrition%20Exam%201/cam-nutrition-master-exam-form-d.html": "2026-07-25",
        "CAM%20Nutrition%20Exam%201/cam-nutrition-master-exam-form-e.html": "2026-07-25",
        "Physical%20Diagnosis%201%20Exam%202/anus-rectum-quiz.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%202/anus-rectum-quiz-version-2.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%202/male-gu-prostate-quiz.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%202/male-gu-prostate-quiz-version-2.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%202/abdominal-exam-quiz.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%202/abdominal-exam-quiz-version-2.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%202/lung-thorax-exam-quiz.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%202/lung-thorax-exam-quiz-version-2.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%202/skin-hair-nail-exam-quiz.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%202/skin-hair-nail-exam-quiz-version-2.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%202/eye-exam-quiz.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%202/eye-exam-quiz-version-2.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%202/general-survey-vitals-quiz.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%202/general-survey-vitals-quiz-version-2.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%202/cardio-pv-exam-quiz.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%202/cardio-pv-exam-quiz-version-2.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%202/hent-exam-quiz.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%202/hent-exam-quiz-version-2.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%202/pd1-exam2-master-exam-form-a.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%202/pd1-exam2-master-exam-form-b.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%202/pd1-exam2-master-exam-form-c.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%202/pd1-exam2-master-exam-form-d.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%202/pd1-exam2-master-exam-form-e.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%202/pd1-exam2-study-guide.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%203/pelvic-exam-quiz.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%203/pelvic-exam-quiz-version-2.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%203/breast-exam-quiz.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%203/breast-exam-quiz-version-2.html": "2026-07-18",
        "Physical%20Diagnosis%201%20Exam%203/musculoskeletal-exam-quiz.html": "2026-07-22",
        "Physical%20Diagnosis%201%20Exam%203/musculoskeletal-exam-quiz-version-2.html": "2026-07-22",
        "Physical%20Diagnosis%201%20Exam%203/neuro-exam-quiz.html": "2026-07-22",
        "Physical%20Diagnosis%201%20Exam%203/neuro-exam-quiz-version-2.html": "2026-07-22",
        "Physical%20Diagnosis%201%20Exam%203/pd1-exam3-study-guide.html": "2026-07-18",
        "Physiology%20Exam%203/hemostasis-quiz-version-4.html": "2026-07-18",
        "Physiology%20Exam%203/hemostasis-quiz-version-5.html": "2026-07-18",
        "Physiology%20Exam%203/immunology-quiz-version-4.html": "2026-07-18",
        "Physiology%20Exam%203/immunology-quiz-version-5.html": "2026-07-18",
        "Physiology%20Exam%203/pulmonary-quiz-version-4.html": "2026-07-18",
        "Physiology%20Exam%203/pulmonary-quiz-version-5.html": "2026-07-18",
        "Physiology%20Exam%203/gi-quiz-version-4.html": "2026-07-18",
        "Physiology%20Exam%203/gi-quiz-version-5.html": "2026-07-18",
        "Physiology%20Exam%203/metabolism-quiz-version-4.html": "2026-07-18",
        "Physiology%20Exam%203/metabolism-quiz-version-5.html": "2026-07-18",
        "Physiology%20Exam%203/physiology-master-exam-version-11.html": "2026-07-18",
        "Physiology%20Exam%203/physiology-master-exam-version-12.html": "2026-07-18",
        "Anatomy%20Exam%201/intro-anatomy-quiz.html": "2026-07-16",
        "Anatomy%20Exam%201/intro-anatomy-quiz-version-2.html": "2026-07-16",
        "Anatomy%20Exam%201/histology-quiz.html": "2026-07-16",
        "Anatomy%20Exam%201/histology-quiz-version-2.html": "2026-07-16",
        "Anatomy%20Exam%201/brain-ans-quiz.html": "2026-07-16",
        "Anatomy%20Exam%201/brain-ans-quiz-version-2.html": "2026-07-16",
        "Anatomy%20Exam%201/nervous-tissue-cbf-quiz.html": "2026-07-16",
        "Anatomy%20Exam%201/nervous-tissue-cbf-quiz-version-2.html": "2026-07-16",
        "Anatomy%20Exam%201/spinal-cord-sensory-quiz.html": "2026-07-16",
        "Anatomy%20Exam%201/spinal-cord-sensory-quiz-version-2.html": "2026-07-16",
        "Anatomy%20Exam%201/peripheral-cranial-nerves-quiz.html": "2026-07-16",
        "Anatomy%20Exam%201/peripheral-cranial-nerves-quiz-version-2.html": "2026-07-16",
        "Anatomy%20Exam%201/anatomy-master-exam-form-a.html": "2026-07-16",
        "Anatomy%20Exam%201/anatomy-master-exam-form-b.html": "2026-07-16",
        "Anatomy%20Exam%201/anatomy-master-exam-form-c.html": "2026-07-16",
        "Anatomy%20Exam%201/anatomy-master-exam-form-d.html": "2026-07-16",
        "Anatomy%20Exam%201/anatomy-master-exam-form-e.html": "2026-07-16",
        "Anatomy%20Exam%201/anatomy-exam-1-study-guide.html": "2026-07-16",
        "Anatomy%20Exam%202/integumentary-system-quiz.html": "2026-07-16",
        "Anatomy%20Exam%202/integumentary-system-quiz-version-2.html": "2026-07-16",
        "Anatomy%20Exam%202/eye-ear-anatomy-quiz.html": "2026-07-16",
        "Anatomy%20Exam%202/eye-ear-anatomy-quiz-version-2.html": "2026-07-16",
        "Anatomy%20Exam%202/heart-great-vessels-quiz.html": "2026-07-16",
        "Anatomy%20Exam%202/heart-great-vessels-quiz-version-2.html": "2026-07-16",
        "Anatomy%20Exam%202/vascular-lymphatics-quiz.html": "2026-07-16",
        "Anatomy%20Exam%202/vascular-lymphatics-quiz-version-2.html": "2026-07-16",
        "Anatomy%20Exam%202/pulmonary-anatomy-quiz.html": "2026-07-16",
        "Anatomy%20Exam%202/pulmonary-anatomy-quiz-version-2.html": "2026-07-16",
        "Anatomy%20Exam%202/anatomy-master-exam-form-a.html": "2026-07-16",
        "Anatomy%20Exam%202/anatomy-master-exam-form-b.html": "2026-07-16",
        "Anatomy%20Exam%202/anatomy-master-exam-form-c.html": "2026-07-16",
        "Anatomy%20Exam%202/anatomy-master-exam-form-d.html": "2026-07-16",
        "Anatomy%20Exam%202/anatomy-master-exam-form-e.html": "2026-07-16",
        "Anatomy%20Exam%202/anatomy-exam-2-study-guide.html": "2026-07-16",
        "Physiology%20Exam%201/cell-physiology-membranes-quiz.html": "2026-07-16",
        "Physiology%20Exam%201/cell-physiology-membranes-quiz-version-2.html": "2026-07-16",
        "Physiology%20Exam%201/membrane-potentials-action-potentials-quiz.html": "2026-07-16",
        "Physiology%20Exam%201/membrane-potentials-action-potentials-quiz-version-2.html": "2026-07-16",
        "Physiology%20Exam%201/nervous-system-sensory-quiz.html": "2026-07-16",
        "Physiology%20Exam%201/nervous-system-sensory-quiz-version-2.html": "2026-07-16",
        "Physiology%20Exam%201/nervous-system-motor-quiz.html": "2026-07-16",
        "Physiology%20Exam%201/nervous-system-motor-quiz-version-2.html": "2026-07-16",
        "Physiology%20Exam%201/cns-function-quiz.html": "2026-07-16",
        "Physiology%20Exam%201/cns-function-quiz-version-2.html": "2026-07-16",
        "Physiology%20Exam%201/physiology-master-exam-form-a.html": "2026-07-16",
        "Physiology%20Exam%201/physiology-master-exam-form-b.html": "2026-07-16",
        "Physiology%20Exam%201/physiology-master-exam-form-c.html": "2026-07-16",
        "Physiology%20Exam%201/physiology-master-exam-form-d.html": "2026-07-16",
        "Physiology%20Exam%201/physiology-master-exam-form-e.html": "2026-07-16",
        "Physiology%20Exam%201/physiology-exam-1-study-guide.html": "2026-07-16",
        "Physiology%20Exam%202/hearing-taste-smell-quiz.html": "2026-07-16",
        "Physiology%20Exam%202/hearing-taste-smell-quiz-version-2.html": "2026-07-16",
        "Physiology%20Exam%202/cardiac-physiology-quiz.html": "2026-07-16",
        "Physiology%20Exam%202/cardiac-physiology-quiz-version-2.html": "2026-07-16",
        "Physiology%20Exam%202/circulatory-physiology-1-quiz.html": "2026-07-16",
        "Physiology%20Exam%202/circulatory-physiology-1-quiz-version-2.html": "2026-07-16",
        "Physiology%20Exam%202/circulatory-physiology-2-quiz.html": "2026-07-16",
        "Physiology%20Exam%202/circulatory-physiology-2-quiz-version-2.html": "2026-07-16",
        "Physiology%20Exam%202/physiology-of-vision-quiz.html": "2026-07-16",
        "Physiology%20Exam%202/physiology-of-vision-quiz-version-2.html": "2026-07-16",
        "Physiology%20Exam%202/physiology-master-exam-form-a.html": "2026-07-16",
        "Physiology%20Exam%202/physiology-master-exam-form-b.html": "2026-07-16",
        "Physiology%20Exam%202/physiology-master-exam-form-c.html": "2026-07-16",
        "Physiology%20Exam%202/physiology-master-exam-form-d.html": "2026-07-16",
        "Physiology%20Exam%202/physiology-master-exam-form-e.html": "2026-07-16",
        "Physiology%20Exam%202/physiology-exam-2-study-guide.html": "2026-07-16",
        "Physiology%20Exam%203/physiology-master-exam-version-5.html": "2026-07-08",
        "Physiology%20Exam%203/physiology-master-exam-version-6.html": "2026-07-08",
        "Physiology%20Exam%203/physiology-master-exam-version-7.html": "2026-07-08",
        "Physiology%20Exam%203/physiology-master-exam-version-8.html": "2026-07-08",
        "Physiology%20Exam%203/physiology-master-exam-version-9.html": "2026-07-08",
        "Physiology%20Exam%203/physiology-master-exam-version-10.html": "2026-07-09",
        "Physiology%20Exam%203/hemostasis-quiz-version-2.html": "2026-07-08",
        "Physiology%20Exam%203/hemostasis-quiz-version-3.html": "2026-07-08",
        "Physiology%20Exam%203/immunology-quiz-version-2.html": "2026-07-08",
        "Physiology%20Exam%203/immunology-quiz-version-3.html": "2026-07-08",
        "Physiology%20Exam%203/gi-quiz-version-2.html": "2026-07-08",
        "Physiology%20Exam%203/gi-quiz-version-3.html": "2026-07-08",
        "Physiology%20Exam%203/metabolism-quiz-version-2.html": "2026-07-08",
        "Physiology%20Exam%203/metabolism-quiz-version-3.html": "2026-07-08",
        "Physiology%20Exam%203/pulmonary-quiz-version-2.html": "2026-07-08",
        "Physiology%20Exam%203/pulmonary-quiz-version-3.html": "2026-07-08",
        "Physiology%20Exam%204/Renal_Physiology_I_Quiz.html": "2026-07-11",
        "Physiology%20Exam%204/Renal_II_Comprehensive_Quiz.html": "2026-07-11",
        "Anatomy%20Exam%203/endocrine-quiz-version-2.html": "2026-07-11",
        "Anatomy%20Exam%203/gi-i-ii-quiz-version-2.html": "2026-07-11",
        "Anatomy%20Exam%203/female-reproductive-quiz-version-2.html": "2026-07-11",
        "Anatomy%20Exam%203/male-reproductive-quiz-version-2.html": "2026-07-11",
        "Anatomy%20Exam%203/nephrology-urinary-quiz.html": "2026-07-11",
        "Anatomy%20Exam%203/endocrine-quiz-version-3.html": "2026-07-11",
        "Anatomy%20Exam%203/endocrine-quiz-version-4.html": "2026-07-11",
        "Anatomy%20Exam%203/gi-i-ii-quiz-version-3.html": "2026-07-11",
        "Anatomy%20Exam%203/gi-i-ii-quiz-version-4.html": "2026-07-11",
        "Anatomy%20Exam%203/female-reproductive-quiz-version-3.html": "2026-07-11",
        "Anatomy%20Exam%203/female-reproductive-quiz-version-4.html": "2026-07-11",
        "Anatomy%20Exam%203/male-reproductive-quiz-version-3.html": "2026-07-11",
        "Anatomy%20Exam%203/male-reproductive-quiz-version-4.html": "2026-07-11",
        "Anatomy%20Exam%203/nephrology-urinary-quiz-version-2.html": "2026-07-11",
        "Anatomy%20Exam%203/nephrology-urinary-quiz-version-3.html": "2026-07-11",
        "Anatomy%20Exam%203/anatomy-master-exam-form-a.html": "2026-07-11",
        "Anatomy%20Exam%203/anatomy-master-exam-form-b.html": "2026-07-11",
        "Anatomy%20Exam%203/anatomy-master-exam-form-c.html": "2026-07-11",
        "Anatomy%20Exam%203/anatomy-master-exam-form-d.html": "2026-07-11",
        "Anatomy%20Exam%203/anatomy-master-exam-form-e.html": "2026-07-11",
        "Physiology%20Exam%204/endo-iii-exam1-male-reproductive.html": "2026-07-13",
        "Physiology%20Exam%204/endo-iii-exam2-female-pregnancy-lactation.html": "2026-07-13",
        "Physiology%20Exam%204/endo1_practice_quiz.html": "2026-07-13",
        "Physiology%20Exam%204/endo2_part1_adrenal_quiz.html": "2026-07-13",
        "Physiology%20Exam%204/endo2_part2_quiz.html": "2026-07-13",
        "Intro%20to%20PA%20Profession/pa-intro-master-exam-form-a.html": "2026-07-13",
        "Intro%20to%20PA%20Profession/pa-intro-master-exam-form-b.html": "2026-07-13",
        "Intro%20to%20PA%20Profession/pa-intro-master-exam-form-c.html": "2026-07-13",
        "Intro%20to%20PA%20Profession/pa-intro-master-exam-form-d.html": "2026-07-13",
        "Intro%20to%20PA%20Profession/pa-intro-master-exam-form-e.html": "2026-07-13",
        "Nutrition%20Class/nutrition-ppt-1-2-review-qs.html": "2026-07-14",
        "Anatomy%20Exam%203/endocrine-quiz-version-5.html": "2026-07-14",
        "Anatomy%20Exam%203/female-reproductive-quiz-version-5.html": "2026-07-14",
        "Anatomy%20Exam%203/gi-i-ii-quiz-version-5.html": "2026-07-14",
        "Anatomy%20Exam%203/male-reproductive-quiz-version-5.html": "2026-07-14",
        "Anatomy%20Exam%203/nephrology-urinary-quiz-version-4.html": "2026-07-14",
        "CAM%20Nutrition%20Exam%201/human-nutrition-quiz.html": "2026-07-14",
        "CAM%20Nutrition%20Exam%201/human-nutrition-quiz-version-2.html": "2026-07-14",
        "CAM%20Nutrition%20Exam%201/macronutrients-micronutrients-water-quiz.html": "2026-07-14",
        "CAM%20Nutrition%20Exam%201/macronutrients-micronutrients-water-quiz-version-2.html": "2026-07-14",
        "Physiology%20Exam%204/renal-physiology-1-quiz.html": "2026-07-16",
        "Physiology%20Exam%204/renal-physiology-1-quiz-version-2.html": "2026-07-16",
        "Physiology%20Exam%204/renal-physiology-2-quiz.html": "2026-07-16",
        "Physiology%20Exam%204/renal-physiology-2-quiz-version-2.html": "2026-07-16",
        "Physiology%20Exam%204/endocrine-physiology-1-quiz.html": "2026-07-16",
        "Physiology%20Exam%204/endocrine-physiology-1-quiz-version-2.html": "2026-07-16",
        "Physiology%20Exam%204/endocrine-physiology-2-quiz.html": "2026-07-16",
        "Physiology%20Exam%204/endocrine-physiology-2-quiz-version-2.html": "2026-07-16",
        "Physiology%20Exam%204/endocrine-physiology-3-quiz.html": "2026-07-16",
        "Physiology%20Exam%204/endocrine-physiology-3-quiz-version-2.html": "2026-07-16",
        "CAM%20Nutrition%20Exam%201/special-topics-nutrition-quiz.html": "2026-07-16",
        "CAM%20Nutrition%20Exam%201/special-topics-nutrition-quiz-version-2.html": "2026-07-16",
        "CAM%20Nutrition%20Exam%201/weight-control-quiz.html": "2026-07-16",
        "CAM%20Nutrition%20Exam%201/weight-control-quiz-version-2.html": "2026-07-16",
        "Anatomy%20Exam%204/appendicular-skeleton-quiz.html": "2026-07-16",
        "Anatomy%20Exam%204/appendicular-skeleton-quiz-version-2.html": "2026-07-16",
        "Anatomy%20Exam%204/axial-skeleton-quiz.html": "2026-07-16",
        "Anatomy%20Exam%204/axial-skeleton-quiz-version-2.html": "2026-07-16",
        "Anatomy%20Exam%204/appendicular-musculature-quiz.html": "2026-07-16",
        "Anatomy%20Exam%204/appendicular-musculature-quiz-version-2.html": "2026-07-16",
        "Anatomy%20Exam%204/axial-musculature-quiz.html": "2026-07-16",
        "Anatomy%20Exam%204/axial-musculature-quiz-version-2.html": "2026-07-16",
        "Anatomy%20Exam%204/appendicular-skeleton-quiz-version-3.html": "2026-07-21",
        "Anatomy%20Exam%204/appendicular-skeleton-quiz-version-4.html": "2026-07-21",
        "Anatomy%20Exam%204/axial-skeleton-quiz-version-3.html": "2026-07-21",
        "Anatomy%20Exam%204/axial-skeleton-quiz-version-4.html": "2026-07-21",
        "Anatomy%20Exam%204/appendicular-musculature-quiz-version-3.html": "2026-07-21",
        "Anatomy%20Exam%204/appendicular-musculature-quiz-version-4.html": "2026-07-21",
        "Anatomy%20Exam%204/axial-musculature-quiz-version-3.html": "2026-07-21",
        "Anatomy%20Exam%204/axial-musculature-quiz-version-4.html": "2026-07-21",
        "Anatomy%20Exam%204/anatomical-position-relationships-quiz.html": "2026-07-21",
        "Anatomy%20Exam%204/anatomical-position-relationships-quiz-version-2.html": "2026-07-21",
        "Anatomy%20Exam%204/anatomy-master-exam-form-a.html": "2026-07-21",
        "Anatomy%20Exam%204/anatomy-master-exam-form-b.html": "2026-07-21",
        "Anatomy%20Exam%204/anatomy-master-exam-form-c.html": "2026-07-21",
        "Anatomy%20Exam%204/anatomy-master-exam-form-d.html": "2026-07-21",
        "Anatomy%20Exam%204/anatomy-master-exam-form-e.html": "2026-07-21",
        "Anatomy%20Exam%203/endocrine-quiz-version-6.html": "2026-07-16",
        "Anatomy%20Exam%203/endocrine-quiz-version-7.html": "2026-07-16",
        "Anatomy%20Exam%203/gi-i-ii-quiz-version-6.html": "2026-07-16",
        "Anatomy%20Exam%203/gi-i-ii-quiz-version-7.html": "2026-07-16",
        "Anatomy%20Exam%203/female-reproductive-quiz-version-6.html": "2026-07-16",
        "Anatomy%20Exam%203/female-reproductive-quiz-version-7.html": "2026-07-16",
        "Anatomy%20Exam%203/male-reproductive-quiz-version-6.html": "2026-07-16",
        "Anatomy%20Exam%203/male-reproductive-quiz-version-7.html": "2026-07-16",
        "Anatomy%20Exam%203/nephrology-urinary-quiz-version-5.html": "2026-07-16",
        "Anatomy%20Exam%203/nephrology-urinary-quiz-version-6.html": "2026-07-16",
        "Anatomy%20Exam%203/anatomy-master-exam-form-f.html": "2026-07-16",
        "Anatomy%20Exam%203/anatomy-master-exam-form-g.html": "2026-07-16"
      };
      var NEW_BADGE_DAYS = 3;
      var now = Date.now();

      document.querySelectorAll("a.quiz-link").forEach((a) => {
        const added = NEW_QUIZZES[a.getAttribute("href")];
        if (!added) return;
        const addedMs = new Date(added + "T00:00:00").getTime();
        if ((now - addedMs) / 86400000 > NEW_BADGE_DAYS) return;
        const badge = document.createElement("span");
        badge.className = "new-badge";
        badge.textContent = "NEW";
        // Insert right after the title text, not appended last -- the score
        // badge (added earlier, above) has margin-left:auto to pin itself to
        // the far right of the pill. Appending NEW after it put both badges
        // stacked together on the right, which read as cluttered. Keeping
        // NEW next to the title and letting the score badge own the right
        // edge on its own keeps every pill's score in the same spot.
        const scoreBadge = a.querySelector(".score-badge");
        if (scoreBadge) a.insertBefore(badge, scoreBadge);
        else a.appendChild(badge);
      });
    })();

/* ---- from index.html (was inline at line 2246) ---- */
(function () {
      // Curated set of "special" quizzes (currently: from Ricky) -- unlike
      // NEW_QUIZZES above, this list never expires by date. Add a quiz's
      // href here whenever one should be flagged; no removal needed later.
      var R_QUIZZES = {
        "Physiology%20Exam%204/Renal_Physiology_I_Quiz.html": true,
        "Physiology%20Exam%204/Renal_II_Comprehensive_Quiz.html": true,
        "Physiology%20Exam%204/endo-iii-exam1-male-reproductive.html": true,
        "Physiology%20Exam%204/endo-iii-exam2-female-pregnancy-lactation.html": true,
        "Physiology%20Exam%204/endo1_practice_quiz.html": true,
        "Physiology%20Exam%204/endo2_part1_adrenal_quiz.html": true,
        "Physiology%20Exam%204/endo2_part2_quiz.html": true,
        "Anatomy%20Exam%203/endocrine-quiz-version-5.html": true,
        "Anatomy%20Exam%203/female-reproductive-quiz-version-5.html": true,
        "Anatomy%20Exam%203/gi-i-ii-quiz-version-5.html": true,
        "Anatomy%20Exam%203/male-reproductive-quiz-version-5.html": true,
        "Anatomy%20Exam%203/nephrology-urinary-quiz-version-4.html": true
      };
      document.querySelectorAll("a.quiz-link").forEach((a) => {
        if (!R_QUIZZES[a.getAttribute("href")]) return;
        const badge = document.createElement("span");
        badge.className = "r-badge";
        badge.textContent = "R";
        badge.title = "Special quiz";
        const scoreBadge = a.querySelector(".score-badge");
        if (scoreBadge) a.insertBefore(badge, scoreBadge);
        else a.appendChild(badge);
      });
    })();

/* ---- from index.html (was inline at line 2278) ---- */
(function () {
      const overlay = document.getElementById("archived-modal-overlay");
      function openModal() { overlay.classList.add("open"); }
      function closeModal() { overlay.classList.remove("open"); }
      document.getElementById("archived-open").addEventListener("click", openModal);
      document.getElementById("archived-modal-close").addEventListener("click", closeModal);
      overlay.addEventListener("click", (e) => { if (e.target === overlay) closeModal(); });
      document.addEventListener("keydown", (e) => { if (e.key === "Escape" && overlay.classList.contains("open")) closeModal(); });
    })();

/* ---- from index.html (was inline at line 2290) ---- */
(function () {
      const overlay = document.getElementById("whatsnew-modal-overlay");
      function openModal() { overlay.classList.add("open"); }
      function closeModal() { overlay.classList.remove("open"); }
      document.getElementById("whatsnew-open").addEventListener("click", openModal);
      document.getElementById("whatsnew-modal-close").addEventListener("click", closeModal);
      overlay.addEventListener("click", (e) => { if (e.target === overlay) closeModal(); });
      document.addEventListener("keydown", (e) => { if (e.key === "Escape" && overlay.classList.contains("open")) closeModal(); });
    })();

/* ---- from index.html (was inline at line 2301) ---- */
if ("serviceWorker" in navigator) {
      const hadController = !!navigator.serviceWorker.controller;
      function showSWUpdateBanner() {
        if (document.getElementById("sw-update-banner")) return;
        const bar = document.createElement("div");
        bar.id = "sw-update-banner";
        bar.style.cssText = "position:fixed;top:0;left:0;right:0;z-index:4000;background:#2563eb;color:#fff;text-align:center;font:600 13px/1.4 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;padding:10px 16px;";
        bar.innerHTML = "A new version of this site is available. <button style=\"margin-left:10px;background:#fff;color:#2563eb;border:none;border-radius:6px;padding:5px 12px;font-weight:700;cursor:pointer;font-size:13px;\">Refresh</button>";
        bar.querySelector("button").addEventListener("click", () => location.reload());
        document.body.prepend(bar);
      }
      navigator.serviceWorker.addEventListener("controllerchange", () => {
        if (hadController) showSWUpdateBanner();
      });
      window.addEventListener("load", () => { navigator.serviceWorker.register("sw.js").catch(() => {}); });
    }

/* ---- from index.html (was inline at line 2320) ---- */
function showToast(message, duration) {
      duration = duration || 3000;
      let toast = document.getElementById("site-toast");
      if (!toast) {
        toast = document.createElement("div");
        toast.id = "site-toast";
        toast.style.cssText = "position:fixed;bottom:24px;left:50%;transform:translateX(-50%);background:#111827;color:#fff;padding:10px 18px;border-radius:999px;font:600 13px -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;z-index:5000;box-shadow:0 6px 20px rgba(0,0,0,.3);opacity:0;transition:opacity .2s var(--ease);max-width:80vw;text-align:center;";
        document.body.appendChild(toast);
      }
      toast.textContent = message;
      requestAnimationFrame(() => { toast.style.opacity = "1"; });
      clearTimeout(toast._hideTimer);
      toast._hideTimer = setTimeout(() => { toast.style.opacity = "0"; }, duration);
    }

    (function () {
      const btn = document.getElementById("install-app-btn");
      let deferredPrompt = null;

      function isStandalone() {
        return window.matchMedia("(display-mode: standalone)").matches || window.navigator.standalone === true;
      }
      function isIOS() {
        return /iphone|ipad|ipod/i.test(navigator.userAgent) && !window.MSStream;
      }
      if (isStandalone()) btn.style.display = "none";

      window.addEventListener("beforeinstallprompt", (e) => {
        e.preventDefault();
        deferredPrompt = e;
        setTimeout(() => maybeShowBanner("android"), 1200);
      });

      window.addEventListener("appinstalled", () => {
        deferredPrompt = null;
        btn.style.display = "none";
        dismissBanner();
        showToast("Installed! Find it on your home screen.");
      });

      btn.addEventListener("click", async () => {
        if (deferredPrompt) {
          try {
            deferredPrompt.prompt();
            await deferredPrompt.userChoice;
            deferredPrompt = null;
            return;
          } catch (err) {
            // fall through to manual-instructions toast
          }
        }
        showToast('To install: open your browser menu and choose "Add to Home Screen" or "Install App".', 4500);
      });

      const installIconSvg = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12"/><path d="M7 10l5 5 5-5"/><path d="M4 19h16"/></svg>';
      let banner = null;

      function hideBanner() {
        if (banner) banner.classList.remove("show");
      }
      function dismissBanner() {
        localStorage.setItem("installBannerDismissed", "1");
        hideBanner();
      }
      function maybeShowBanner(platform) {
        if (isStandalone() || localStorage.getItem("installBannerDismissed") || banner) return;
        banner = document.createElement("div");
        banner.className = "install-banner";
        banner.innerHTML = platform === "ios"
          ? '<div class="install-banner-icon">' + installIconSvg + '</div>' +
            '<div class="install-banner-body">' +
              '<p class="install-banner-title">Install this site as an app</p>' +
              '<p class="install-banner-text">Tap the Share icon, then &ldquo;Add to Home Screen&rdquo;, for quick offline access to your quizzes.</p>' +
              '<div class="install-banner-actions"><button type="button" class="install-banner-btn primary" id="install-banner-ok">Got it</button></div>' +
            '</div>' +
            '<button type="button" class="install-banner-close" id="install-banner-close" aria-label="Dismiss">&times;</button>'
          : '<div class="install-banner-icon">' + installIconSvg + '</div>' +
            '<div class="install-banner-body">' +
              '<p class="install-banner-title">Install this site as an app</p>' +
              '<p class="install-banner-text">Get quick, offline access to your quizzes right from your home screen.</p>' +
              '<div class="install-banner-actions">' +
                '<button type="button" class="install-banner-btn primary" id="install-banner-install">Install</button>' +
                '<button type="button" class="install-banner-btn" id="install-banner-ok">Not now</button>' +
              '</div>' +
            '</div>' +
            '<button type="button" class="install-banner-close" id="install-banner-close" aria-label="Dismiss">&times;</button>';
        document.body.appendChild(banner);
        setTimeout(() => banner.classList.add("show"), 50);

        banner.querySelector("#install-banner-close").addEventListener("click", dismissBanner);
        const okBtn = banner.querySelector("#install-banner-ok");
        if (okBtn) okBtn.addEventListener("click", dismissBanner);
        const installBtn = banner.querySelector("#install-banner-install");
        if (installBtn) {
          installBtn.addEventListener("click", async () => {
            dismissBanner();
            if (deferredPrompt) {
              try {
                deferredPrompt.prompt();
                await deferredPrompt.userChoice;
                deferredPrompt = null;
              } catch (err) {}
            }
          });
        }
      }

      if (isIOS() && !isStandalone()) {
        setTimeout(() => maybeShowBanner("ios"), 2500);
      }
    })();

/* ---- from index.html (was inline at line 2434) ---- */
function buildHomeTourSteps() {
      var steps = [
        { selector: "#site-search", title: "Search everything", text: "Search every quiz on the site by name from right here." },
        { selector: "#week-widget", title: "This week", text: "See this week's exams and practicums at a glance — it automatically moves to next week every Friday at 5pm." }
      ];
      var continueWidget = document.getElementById("continue-widget");
      if (continueWidget && !continueWidget.classList.contains("hidden")) {
        steps.push({ selector: "#continue-widget", title: "Continue where you left off", text: "Quizzes you've started but haven't finished show up here." });
      }
      steps.push({ selector: ".tabs", title: "Switch classes", text: "Jump between Physiology, Pharmacodynamics, Anatomy, and Anatomy Practicum here." });
      steps.push({ selector: null, title: "One more thing", text: "Open any quiz to find a shuffle toggle, a pause/resume timer, and a keyboard-shortcuts button too. Good luck studying!" });
      return steps;
    }

    document.addEventListener("DOMContentLoaded", function () {
      document.getElementById("tour-open").addEventListener("click", function () {
        if (window.SiteTour) window.SiteTour.run(buildHomeTourSteps(), "tourSeen:home");
      });

      function tryStartTour(attemptsLeft) {
        if (!window.SiteTour) return;
        if (document.querySelector(".install-banner.show") && attemptsLeft > 0) {
          setTimeout(function () { tryStartTour(attemptsLeft - 1); }, 1500);
          return;
        }
        window.SiteTour.start(buildHomeTourSteps(), "tourSeen:home");
      }
      setTimeout(function () { tryStartTour(3); }, 3200);
    });

/* ---- from index.html (was inline at line 2466) ---- */
// Hover flair for the homepage Arcade/Group Study nav buttons, added
    // 2026-07-18. Purely decorative; skipped under prefers-reduced-motion.
    // Guides' book-icon crossfade is pure CSS (.guides-icon-wrap), no JS
    // needed. href-based selectors grab both the inline .search-wrap button
    // and the rail counterpart in one query -- only one of the pair is ever
    // displayed at a given width, so binding both is harmless.
    (function () {
      function reducedMotion() {
        return window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
      }
      function themeColor(name, fallback) {
        var v = getComputedStyle(document.documentElement).getPropertyValue(name);
        return v ? v.trim() : fallback;
      }

      // --- Arcade: color burst shoots outward on hover ---
      function burstFromButton(btn) {
        if (reducedMotion()) return;
        var rect = btn.getBoundingClientRect();
        var cx = rect.left + rect.width / 2, cy = rect.top + rect.height / 2;
        var colors = [
          themeColor("--accent", "#2a6df2"), themeColor("--accent2", "#218640"),
          themeColor("--accent3", "#9c46f3"), "#f59e0b", "#ec4899"
        ];
        for (var i = 0; i < 16; i++) {
          (function (i) {
            var angle = Math.random() * Math.PI * 2;
            var dist = 46 + Math.random() * 54;
            var size = 5 + Math.random() * 5;
            var piece = document.createElement("div");
            piece.className = "btn-burst-piece";
            piece.style.width = size + "px";
            piece.style.height = size + "px";
            piece.style.left = (cx - size / 2) + "px";
            piece.style.top = (cy - size / 2) + "px";
            piece.style.background = colors[i % colors.length];
            piece.style.setProperty("--bx", (Math.cos(angle) * dist).toFixed(1) + "px");
            piece.style.setProperty("--by", (Math.sin(angle) * dist).toFixed(1) + "px");
            document.body.appendChild(piece);
            setTimeout(function () { piece.remove(); }, 750);
          })(i);
        }
      }
      document.querySelectorAll('a[href="arcade.html"]').forEach(function (btn) {
        btn.addEventListener("mouseenter", function () { burstFromButton(btn); });
      });

      // --- Group Study: small dots converge into the button, like people
      // joining a group ---
      function joinAtButton(btn) {
        if (reducedMotion()) return;
        var rect = btn.getBoundingClientRect();
        var cx = rect.left + rect.width / 2, cy = rect.top + rect.height / 2;
        var colors = [
          themeColor("--accent", "#2a6df2"), themeColor("--accent2", "#218640"),
          themeColor("--accent3", "#9c46f3"), "#f59e0b"
        ];
        var count = 6;
        for (var i = 0; i < count; i++) {
          (function (i) {
            var angle = (Math.PI * 2 * i) / count + Math.random() * 0.4;
            var dist = 60 + Math.random() * 30;
            var size = 12;
            var piece = document.createElement("div");
            piece.className = "btn-avatar-piece";
            piece.style.width = size + "px";
            piece.style.height = size + "px";
            piece.style.left = (cx - size / 2) + "px";
            piece.style.top = (cy - size / 2) + "px";
            piece.style.background = colors[i % colors.length];
            piece.style.border = "2px solid var(--card)";
            piece.style.setProperty("--sx", (Math.cos(angle) * dist).toFixed(1) + "px");
            piece.style.setProperty("--sy", (Math.sin(angle) * dist).toFixed(1) + "px");
            piece.style.animationDelay = (i * 35) + "ms";
            document.body.appendChild(piece);
            setTimeout(function () { piece.remove(); }, 800);
          })(i);
        }
      }
      document.querySelectorAll('a[href="group-join.html"]').forEach(function (btn) {
        btn.addEventListener("mouseenter", function () { joinAtButton(btn); });
      });
    })();

/* ---- Review link: reveal only when there is something to review ---- */
(function () {
  var link = document.getElementById("review-link");
  if (!link) return;
  var n = 0;
  try {
    for (var i = 0; i < localStorage.length; i++) {
      var k = localStorage.key(i);
      if (!k || k.indexOf("qm:") !== 0) continue;
      var rec = JSON.parse(localStorage.getItem(k));
      if (rec && rec.m) n += rec.m.length;
    }
  } catch (e) { return; }
  if (!n) return;
  document.getElementById("review-count").textContent = n;
  link.hidden = false;
})();
