/* The semester dropdown, shared by every page that offers one.

   The homepage, the guides page and the Arcade all need the same control, and
   three hand-rolled copies of a menu is exactly the drift the registry
   (semesters.js) exists to prevent. Styles live in theme.css for the same
   reason -- it is the one stylesheet all three pages already load.

   Usage:
     var picker = window.SemesterPicker({
       semesters: [...],        // registry entries to offer, in order
       activeId: "summer-1-2026",
       onPick: function (id) { ... }   // called only on an actual change
     });
     host.appendChild(picker.el);
     picker.setActive(id);      // reflect a change made somewhere else

   Renders nothing for fewer than two semesters: a one-option menu is noise,
   not navigation, and a control that cannot change anything should not invite
   a click. Callers get back `null` in that case. */
(function () {
  "use strict";

  var CHEVRON = '<svg class="sem-chevron" viewBox="0 0 24 24" width="18" height="18" ' +
    'fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" ' +
    'stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>';

  // one open menu at a time, across every picker on the page
  var openPicker = null;

  function closeOpen() {
    if (!openPicker) return;
    openPicker.wrap.classList.remove("open");
    openPicker.btn.setAttribute("aria-expanded", "false");
    openPicker = null;
  }

  document.addEventListener("click", function (e) {
    if (!e.target.closest(".semester-picker")) closeOpen();
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && openPicker) {
      var btn = openPicker.btn;
      closeOpen();
      btn.focus();
    }
  });

  window.SemesterPicker = function (opts) {
    var sems = (opts && opts.semesters) || [];
    if (sems.length < 2) return null;

    /* The term you are in leads the menu; everything else keeps calendar order
       behind it. Callers hand the list over chronologically, which is right for
       a timeline and wrong for a menu -- it put a finished Summer I above the
       Fall term actually in progress, so the one option you almost always want
       was the one you had to look past.

       Hoisted by date rather than by name, so this stays true at every
       rollover. sort() is stable, so the rest of the list is undisturbed. */
    var reg = window.Semesters;
    var currentId = reg && reg.current ? reg.current().id : null;
    if (currentId) {
      sems = sems.slice().sort(function (a, b) {
        return (b.id === currentId) - (a.id === currentId);
      });
    }

    var activeId = opts.activeId || sems[0].id;

    var wrap = document.createElement("span");
    wrap.className = "semester-picker";

    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "semester-picker-btn";
    btn.setAttribute("aria-haspopup", "true");
    btn.setAttribute("aria-expanded", "false");
    var label = document.createElement("span");
    label.className = "sem-picker-label";
    btn.appendChild(label);
    btn.insertAdjacentHTML("beforeend", CHEVRON);

    var menu = document.createElement("div");
    menu.className = "semester-menu";
    menu.setAttribute("role", "menu");

    var options = {};
    sems.forEach(function (sem) {
      var opt = document.createElement("button");
      opt.type = "button";
      opt.className = "sem-option";
      opt.dataset.sem = sem.id;
      opt.setAttribute("role", "menuitemradio");

      var name = document.createElement("span");
      name.className = "sem-option-name";
      name.textContent = sem.label;
      opt.appendChild(name);

      // a term whose dates are still guesses says so here, so the button
      // itself can stay short
      if (sem.estimated) {
        var note = document.createElement("span");
        note.className = "sem-option-note";
        note.textContent = "dates to be confirmed";
        opt.appendChild(note);
      }

      opt.addEventListener("click", function () {
        closeOpen();
        if (sem.id === activeId) return;      // picking the current one is a no-op
        setActive(sem.id);
        if (opts.onPick) opts.onPick(sem.id);
      });
      options[sem.id] = opt;
      menu.appendChild(opt);
    });

    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      var wasOpen = openPicker && openPicker.wrap === wrap;
      closeOpen();
      if (wasOpen) return;
      wrap.classList.add("open");
      btn.setAttribute("aria-expanded", "true");
      openPicker = { wrap: wrap, btn: btn };
    });

    function setActive(id) {
      var sem = null;
      sems.forEach(function (s) { if (s.id === id) sem = s; });
      if (!sem) return;
      activeId = id;
      label.textContent = sem.label;
      Object.keys(options).forEach(function (k) {
        var on = k === id;
        options[k].classList.toggle("active", on);
        options[k].setAttribute("aria-checked", on ? "true" : "false");
      });
    }

    wrap.appendChild(btn);
    wrap.appendChild(menu);
    setActive(activeId);

    return { el: wrap, setActive: setActive };
  };
})();
