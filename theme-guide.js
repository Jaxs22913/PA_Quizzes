/* theme-guide.js -- study-guide tools (highlighter, text-box notes, Add to Pip / Ask Pip, the phone hero
   "Details" toggle). Split out of theme.js 2026-10-19: both blocks returned at once on any page without
   .guide-back-bar, yet every page downloaded and parsed them (~90 KB). theme.js loads this file only on guide
   pages, in order, before guide-ink.js. Moved verbatim. */

(function () {
  if (!document.querySelector(".guide-back-bar")) return;
  // `document.querySelector(".wrap")` (no scoping) grabs the FIRST match
  // in the whole document -- on the redesigned Anatomy Exam 3 guide, that's
  // a small, unrelated `.wrap` reused as a max-width helper INSIDE the
  // masthead header (a coincidental class-name collision, see
  // feedback_guide_highlighting_ux memory), not the real content container.
  // That silently scoped the entire highlighting feature to a tiny header
  // div with almost no text in it. Every guide's real content wrap is a
  // direct child of <body> by convention (same assumption theme.css's
  // dark-mode invert rule makes via `body > .wrap`) -- match that
  // specifically, falling back to the old unscoped lookup only if no guide
  // follows that convention.
  var wrap = document.querySelector("body > .wrap") || document.querySelector(".wrap");
  if (!wrap) return;

  /* ------------------------------------------------------------------------------------------------
     UNITS. A saved highlight is {idx, start, end, color, note} plus, since 2026-10-15, optional
     q (the highlighted words, to find it again after a guide edit) and g (a group id shared by the
     pieces of one highlight that crosses paragraphs, list items or table cells). start/end are
     character offsets into the text of ONE unit element.

     LEGACY units: HL_UNIT_SELECTOR plus the containment filter below, numbered 0..n. Every highlight
     saved before 2026-10-15 points into exactly this numbering, so NEITHER may ever change. (Some
     guides reuse `.io` as a wrapper around their own <p>/<li>; the filter keeps only the innermost
     match, the same fix the read-aloud engine's buildQueue() makes.)

     EXTRA units (2026-10-15), idx "x0", "x1", ...: everything else that holds text. Before this, the
     highlighter could not touch about 23% of the text in the 119 guides (measured), because only the
     legacy elements were units: every <dt>/<dd> of the CMS eight-point frameworks, every table
     header, figure captions, headings, pearls, and with them about 3,400 bold phrases. A selection
     there, or one that ended in the next paragraph (a triple-click, or a drag that runs past a bold
     phrase at the end of a list item), found "no unit" or "two units" and was refused.
     An extra unit is any element below that is not inside a legacy unit and owns text directly (text
     whose nearest unit-ish ancestor is that element). Numbered at load, in the order of their first
     own text, so the numbering only changes when the guide's own markup changes, like the legacy one.
     Old copies of this script simply skip "x" highlights (units["x3"] is undefined), so the format
     stays backward compatible in both directions.
     ------------------------------------------------------------------------------------------------ */
  var HL_UNIT_SELECTOR = "p, li, .cap, .figcap, .callout, td, .io, .io-head, .io-h";
  // <summary> is left out on purpose: a drag or a click on a highlight there would open or close its
  // accordion. (A legacy unit that holds a summary keeps that text, as it did before.)
  var HL_EXTRA_SELECTOR = "dt, dd, th, caption, figcaption, h1, h2, h3, h4, h5, h6, blockquote, pre, label, " +
    "div, section, article, aside, figure, details, ul, ol, dl, table, thead, tbody, tfoot, tr, main";
  var NO_EXTRA = "nav, header, footer, .guide-back-bar, summary, script, style, noscript, template, svg, button, select, textarea, input, [data-no-hl], .gnote";
  var NO_TEXT = "script, style, noscript, template, svg, button, select, textarea, input, option, [data-no-hl], .gnote";
  var NO_X_TEXT = NO_TEXT + ", summary";   // text no EXTRA unit owns
  var HL_KEY = "guideHl:" + location.pathname;
  var NOTE_KEY = "guideNote:" + location.pathname;
  var COLORS = ["yellow", "green", "pink", "blue"];

  // (keep only matches that contain no other match: the same set as the July 2026 pairwise
  // contains() loop, which took 70-130 ms on the largest guides, by a native descendant query)
  var units = Array.prototype.slice.call(wrap.querySelectorAll(HL_UNIT_SELECTOR)).filter(function (el) {
    return !el.querySelector(HL_UNIT_SELECTOR);
  });
  units.forEach(function (u, i) { u.setAttribute("data-hl-idx", i); });

  var xunits = [];
  (function () {
    var cands = wrap.querySelectorAll(HL_EXTRA_SELECTOR + ", " + HL_UNIT_SELECTOR), i, el;
    for (i = 0; i < cands.length; i++) {
      el = cands[i];
      if (el.closest("[data-hl-idx]") || el.closest(NO_EXTRA)) continue;
      el.__hlc = 1;
    }
    wrap.__hlc = 1;                    // text sitting directly in the content wrap
    var w = document.createTreeWalker(wrap, NodeFilter.SHOW_TEXT, null), n, skip;
    while ((n = w.nextNode())) {
      if (!/\S/.test(n.data)) continue;
      for (el = n.parentElement, skip = false; el; el = el.parentElement) {
        if (el.hasAttribute("data-hl-idx")) break;
        if (el.__hlc) {
          if (!skip && !el.hasAttribute("data-hl-x")) { el.setAttribute("data-hl-x", xunits.length); xunits.push(el); }
          break;
        }
        if (!skip && el.matches(NO_X_TEXT)) skip = true;
        if (el === wrap) break;
      }
    }
  })();

  // The unit that owns this node's text: the nearest legacy unit, or the nearest unit-ish element if
  // it is a numbered extra unit. Text inside a button, svg, form control or note box belongs to no
  // extra unit (it still counts inside a legacy unit, where the July 2026 offsets included it).
  function findUnit(node) {
    var el = node && (node.nodeType === 3 ? node.parentElement : node), skip = false;
    for (; el; el = el.parentElement) {
      if (el.hasAttribute("data-hl-idx")) return el;
      if (el.__hlc) return (!skip && el.hasAttribute("data-hl-x")) ? el : null;
      if (!skip && el.matches(NO_X_TEXT)) skip = true;
      if (el === wrap) return null;
    }
    return null;
  }
  function unitKey(u) {
    return u.hasAttribute("data-hl-idx") ? Number(u.getAttribute("data-hl-idx")) : "x" + u.getAttribute("data-hl-x");
  }
  function unitByKey(k) {
    if (typeof k === "number") return units[k] || null;
    if (typeof k === "string" && /^x\d+$/.test(k)) return xunits[Number(k.slice(1))] || null;
    if (typeof k === "string" && /^\d+$/.test(k)) return units[Number(k)] || null;
    return null;
  }
  var orderedCache = null;
  function ordered() {               // every unit, in document order (built on first use)
    if (!orderedCache) {
      orderedCache = units.concat(xunits).sort(function (a, b) {
        return a === b ? 0 : (a.compareDocumentPosition(b) & 4 ? -1 : 1);
      });
    }
    return orderedCache;
  }

  // A unit's own text nodes, in order. For a legacy unit that is every text node inside it, so its
  // text is exactly its textContent, as in July 2026.
  function ownTexts(u) {
    var out = [], legacy = u.hasAttribute("data-hl-idx");
    var w = document.createTreeWalker(u, NodeFilter.SHOW_TEXT, null), n;
    while ((n = w.nextNode())) if (legacy || findUnit(n) === u) out.push(n);
    return out;
  }
  function unitText(u) {
    var t = ownTexts(u), s = "";
    for (var i = 0; i < t.length; i++) s += t[i].data;
    return s;
  }

  // Character offset, in u's own text, of the boundary point (node, off). A boundary point is not
  // always (textNode, charIndex): triple-click and selections that start or end exactly at an
  // element edge give (element, childIndex), so text nodes are compared by position, not identity.
  function offsetIn(u, node, off) {
    var ts = ownTexts(u), total = 0, r = document.createRange();
    for (var i = 0; i < ts.length; i++) {
      var t = ts[i];
      if (t === node) return total + Math.min(off, t.data.length);
      r.setStart(t, 0); r.collapse(true);
      try { if (r.comparePoint(node, off) <= 0) return total; } catch (e) { return total; }
      total += t.data.length;
    }
    return total;
  }

  // The own text nodes (and the slice of each) that cover [start, end) of u's text.
  function piecesOf(u, start, end) {
    var ts = ownTexts(u), total = 0, out = [];
    for (var i = 0; i < ts.length && total < end; i++) {
      var len = ts[i].data.length, a = Math.max(start, total), b = Math.min(end, total + len);
      if (b > a) out.push({ node: ts[i], s: a - total, e: b - total });
      total += len;
    }
    return out;
  }

  // Wrap [start, end) of u's text in marks made by make(), one per text node it touches, and return
  // them. Never moves or splits an element (the old extractContents() approach cut <strong>, <a>
  // and <mark class="prof-highlight"> in two and could not cross a table cell); only text nodes are
  // split, so every other saved offset stays valid. `skipInside` keeps a new mark from nesting
  // inside an existing one; whitespace between blocks (table rows, list items) is left alone.
  var BLOCKISH_PARENT = "table, thead, tbody, tfoot, tr, ul, ol, dl, select";
  function wrapText(u, start, end, make, skipInside) {
    var out = [];
    piecesOf(u, start, end).forEach(function (p) {
      var parent = p.node.parentElement, txt = p.node.data.slice(p.s, p.e);
      if (!parent || parent.closest(NO_TEXT)) return;
      if (skipInside && parent.closest(skipInside)) return;
      if (!/\S/.test(txt) && (/[\n\r\t]/.test(txt) || parent.matches(BLOCKISH_PARENT))) return;
      var mid = p.s > 0 ? p.node.splitText(p.s) : p.node;
      if (p.e - p.s < mid.data.length) mid.splitText(p.e - p.s);
      var m = make();
      mid.parentNode.insertBefore(m, mid);
      m.appendChild(mid);
      out.push(m);
    });
    return out;
  }
  function unwrap(m) {
    var parent = m.parentNode;
    if (!parent) return;
    while (m.firstChild) parent.insertBefore(m.firstChild, m);
    parent.removeChild(m);
    parent.normalize();
  }

  // A drag-selection landing mid-word used to save exactly that partial-word range, and the mark's
  // padding then drew a color-block edge in the middle of the word. Widen each end to the word
  // boundary, only when that end actually lands mid-word.
  function isWordChar(ch) { return !!ch && /[A-Za-z0-9'’-]/.test(ch); }
  function snapStart(text, start) {
    if (isWordChar(text[start])) while (start > 0 && isWordChar(text[start - 1])) start--;
    return start;
  }
  function snapEnd(text, end) {
    if (isWordChar(text[end - 1])) while (end < text.length && isWordChar(text[end])) end++;
    return end;
  }
  function norm0(t) { return String(t || "").replace(/\s+/g, " ").trim(); }
  function newId(p) { return p + Date.now().toString(36) + Math.random().toString(36).slice(2, 6); }
  // the occurrence of `q` in `text` nearest to `near`, or -1
  function nearestIndex(text, q, near) {
    if (!q) return -1;
    var best = -1, i = text.indexOf(q);
    while (i >= 0) {
      if (best < 0 || Math.abs(i - near) < Math.abs(best - near)) best = i;
      i = text.indexOf(q, i + 1);
    }
    return best;
  }

  // A selection (any Range) as runs of not-yet-highlighted text, one or more per unit, in document
  // order: [{u, start, end}]. Works whatever the range's boundary points are, across units.
  var MAX_SEL_UNITS = 60;
  function runsFrom(range) {
    var root = range.commonAncestorContainer;
    if (root.nodeType !== 1) root = root.parentNode;
    if (!root || !(wrap.contains(root) || root.contains(wrap))) return [];
    if (root.contains(wrap) && root !== wrap) root = wrap;
    var w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null), n, runs = [], seen = [], cur = null;
    var starts = {}, inside = false;
    while ((n = w.nextNode())) {
      if (!range.intersectsNode(n)) { if (inside) break; continue; }    // past the end of the selection
      inside = true;
      var s = n === range.startContainer ? range.startOffset : 0;
      var e = n === range.endContainer ? range.endOffset : n.data.length;
      if (e <= s) continue;
      var u = findUnit(n);
      if (!u) { cur = null; continue; }
      if (n.parentElement && n.parentElement.closest("mark.user-hl")) { cur = null; continue; }
      var ui = seen.indexOf(u);
      if (ui < 0) { seen.push(u); ui = seen.length - 1; starts[ui] = ownTexts(u); }
      // own-text offset of this node inside u
      var ts = starts[ui], base = 0;
      for (var k = 0; k < ts.length && ts[k] !== n; k++) base += ts[k].data.length;
      var a = base + s, b = base + e;
      if (cur && cur.u === u && cur.end === a) cur.end = b;
      else { cur = { u: u, start: a, end: b }; runs.push(cur); }
      if (seen.length > MAX_SEL_UNITS) return runs.concat([null]);    // too big: the caller says so
    }
    return runs;
  }
  function snapRuns(runs) {
    if (!runs.length) return runs;
    var f = runs[0], l = runs[runs.length - 1];
    f.start = snapStart(unitText(f.u), f.start);
    l.end = snapEnd(unitText(l.u), l.end);
    return runs.filter(function (r) { return /\S/.test(unitText(r.u).slice(r.start, r.end)); });
  }
  function runsText(runs) {
    return norm0(runs.map(function (r) { return unitText(r.u).slice(r.start, r.end); }).join(" "));
  }

  /* ------------------------------------------------------------------------------------------------
     HIGHLIGHTS: storage and marks
     ------------------------------------------------------------------------------------------------ */
  function loadHighlights() {
    try { var v = JSON.parse(localStorage.getItem(HL_KEY)); return Array.isArray(v) ? v : []; } catch (e) { return []; }
  }
  function saveHighlights(list) {
    try { localStorage.setItem(HL_KEY, JSON.stringify(list)); return true; }
    catch (e) { if (window.showToast) window.showToast("Could not save your highlight. Check that this browser allows site storage.", 4000); return false; }
  }
  // one highlight = every record sharing this key (a group, or one legacy record)
  function recKey(h) { return h.g ? "g:" + h.g : h.idx + ":" + h.start + ":" + h.end; }
  function recsOf(key) { return loadHighlights().filter(function (h) { return recKey(h) === key; }); }
  function marksOf(key) {
    return Array.prototype.slice.call(wrap.querySelectorAll('mark.user-hl[data-hlk="' + key + '"]'));
  }
  function makeHlMark(color, key) {
    var m = document.createElement("mark");
    m.className = "user-hl user-hl-" + color;
    m.setAttribute("data-hlk", key);
    m.addEventListener("click", function (e) {
      e.stopPropagation(); // don't also trigger the unit's click-to-jump handler
      if (placing) return;
      // a highlight inside a link or an accordion's title: the click opens its options, not the link/accordion
      if (m.closest("a[href], summary")) e.preventDefault();
      var s = window.getSelection();
      if (s && !s.isCollapsed && s.toString().trim()) return;   // the end of a drag, not a click
      openHlPopover(key, m);
    });
    return m;
  }
  // note indicator is CSS-only (mark.has-note::after, see theme.css) rather than an inserted child
  // node: a real node would become part of the unit's text and shift every offset after it.
  function setMarksNote(key, note) {
    var ms = marksOf(key);
    ms.forEach(function (m, i) {
      m.dataset.note = note || "";
      m.classList.toggle("has-note", !!note && i === ms.length - 1);
      m.title = note ? note : "Click to add a note or remove this highlight";
    });
  }
  function applyRec(u, h, key) {
    var ms = wrapText(u, h.start, h.end, function () { return makeHlMark(h.color || "yellow", key); }, "mark.user-hl");
    return ms;
  }
  // Where a saved record sits in the guide as it is now: {u, start, end}, or null when it can't be shown.
  // A record that carries its words (q) and no longer matches them (the guide was edited) is looked for
  // in the same unit and moved, IN MEMORY ONLY: the stored offsets are never rewritten on load (a write
  // before cloud-sync has pulled would stamp this device's copy newer than the cloud's), so the record
  // keeps its key and every later change still finds it. A record without q (saved before 2026-10-15)
  // is applied as it always was, and skipped, as the old engine did, when it no longer fits its unit.
  function placeRec(h) {
    var u = unitByKey(h.idx);
    if (!u || typeof h.start !== "number" || typeof h.end !== "number" || h.start < 0 || h.end <= h.start) return null;
    var txt = unitText(u);
    if (h.q && typeof h.q === "string") {
      if (txt.substr(h.start, h.q.length) === h.q) return { u: u, start: h.start, end: Math.min(h.end, txt.length) };
      var at = nearestIndex(txt, h.q, h.start);
      return at < 0 ? null : { u: u, start: at, end: Math.min(at + (h.end - h.start), txt.length) };
    }
    return h.end > txt.length ? null : { u: u, start: h.start, end: h.end };
  }
  function textOfRecs(recs) {
    return norm0(recs.map(function (h) {
      var pl = placeRec(h);
      return pl ? unitText(pl.u).slice(pl.start, pl.end) : (h.q || "");
    }).join(" "));
  }

  // Restore. Wrapping only splits text nodes, so the order of restoring no longer matters. Nothing is
  // written here.
  (function () {
    var keys = {};
    loadHighlights().forEach(function (h) {
      var pl = placeRec(h);
      if (!pl) return;                 // its words are gone, or it no longer fits: keep the record, show nothing
      var key = recKey(h);
      applyRec(pl.u, { start: pl.start, end: pl.end, color: h.color }, key);
      keys[key] = h.note || "";
    });
    Object.keys(keys).forEach(function (k) { setMarksNote(k, keys[k]); });
  })();

  function createHighlight(range, color) {
    var runs = runsFrom(range);
    if (runs.length && runs[runs.length - 1] === null) return null;
    runs = snapRuns(runs);
    if (!runs.length) return null;
    var g = runs.length > 1 ? newId("g") : null, recs = [];
    runs.forEach(function (r) {
      var rec = { idx: unitKey(r.u), start: r.start, end: r.end, color: color, note: "",
                  q: unitText(r.u).slice(r.start, r.end).slice(0, 200) };
      if (g) rec.g = g;
      recs.push(rec);
    });
    var key = recKey(recs[0]);
    recs.forEach(function (rec, i) { applyRec(runs[i].u, rec, key); });
    setMarksNote(key, "");
    var list = loadHighlights().concat(recs);
    saveHighlights(list);
    // Only a genuinely new highlight is pushed out, never the replay on load. Position only
    // (idx/start/end); color and note never leave this device -- see sharedHl below and firestore.rules.
    if (sharedHl.enabled && sharedHl.uid) recs.forEach(function (h) { sharedHl.pushDoc(h.idx, h.start, h.end); });
    return key;
  }
  function removeHighlight(key) {
    marksOf(key).forEach(unwrap);
    var gone = [];
    saveHighlights(loadHighlights().filter(function (h) {
      if (recKey(h) === key) { gone.push(h); return false; }
      return true;
    }));
    if (sharedHl.enabled && sharedHl.uid) gone.forEach(function (h) { sharedHl.deleteDoc(h.idx, h.start, h.end); });
  }
  function updateRecs(key, fields) {
    var list = loadHighlights();
    list.forEach(function (h) { if (recKey(h) === key) for (var f in fields) h[f] = fields[f]; });
    saveHighlights(list);
  }

  /* ------------------------------------------------------------------------------------------------
     TEXT-BOX NOTES (2026-10-15). A typed note pinned at one spot in the guide. Made only on purpose:
     the "Add a note" tool in the guide toolbar (then click the spot), or "Note" on the selection
     toolbar (pinned where the selection ends). Never from an ordinary click or selection.
     Stored per page under "guideNote:" + location.pathname, an ordinary synced key (cloud-sync.js
     uploads it like the highlights). Written only when a note is saved or deleted, never per keystroke.
     Record: {id, u (unit key), o (offset in that unit's text), b / a (up to 24 characters of guide
     text before / after the spot, to find it again after a guide edit), t (the note), at, m}.
     The box is an empty <span class="gnote"> whose words are drawn by CSS (::after, attr(data-text)):
     it holds no text node, so it never shifts a highlight offset, never shows up in the guide's search,
     read-aloud, copy and paste or Pip's passage matching, and reflows with the text it sits in (phone
     width, accordions opening and closing). Shown when printing, in plain ink.
     ------------------------------------------------------------------------------------------------ */
  var NOTE_MAX = 2000, NOTE_CTX = 24;
  function rawNotes() {
    try { var v = JSON.parse(localStorage.getItem(NOTE_KEY)); return Array.isArray(v) ? v : []; } catch (e) { return []; }
  }
  // the notes themselves; a deleted note's tombstone {id, x} stays in storage only (window.SyncList)
  function loadNotes() { return rawNotes().filter(function (n) { return !window.SyncList.isTomb(n); }); }
  // `gone`: ids deleted just now, kept as tombstones so a sync from another device cannot bring them back
  function saveNotes(list, gone) {
    var now = Date.now(), tombs = rawNotes().filter(window.SyncList.isTomb);
    (gone || []).forEach(function (id) { tombs.push({ id: id, x: now }); });
    list = window.SyncList.pack(list, tombs, now);
    try {
      if (list.length) localStorage.setItem(NOTE_KEY, JSON.stringify(list));
      else localStorage.removeItem(NOTE_KEY);
      return true;
    } catch (e) {
      if (window.showToast) window.showToast("Could not save your note. Check that this browser allows site storage.", 4000);
      return false;
    }
  }
  function noteRec(id) { return loadNotes().filter(function (n) { return n.id === id; })[0] || null; }
  function hostOf(id) { return wrap.querySelector('.gnote[data-gnote="' + id + '"]'); }
  function setHostText(h, t) {
    h.setAttribute("data-text", t || "");
    h.setAttribute("aria-label", t ? "Your note: " + t + ". Press Enter to edit it." : "New note");
    h.title = t ? "Your note (click to edit)" : "New note";
  }
  function makeHost(n) {
    var h = document.createElement("span");
    h.className = "gnote";
    h.setAttribute("data-gnote", n.id);
    h.setAttribute("role", "button");
    h.tabIndex = 0;
    setHostText(h, n.t);
    h.addEventListener("click", function (e) {
      e.preventDefault(); e.stopPropagation();       // not the link, accordion or highlight it sits in
      if (placing) return;
      openNoteEditor(n.id, null);
    });
    h.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") { e.preventDefault(); e.stopPropagation(); openNoteEditor(n.id, null); }
    });
    return h;
  }
  // put a node at offset o of u's text (between characters, never inside a word unless o is)
  function insertAt(u, o, node) {
    var ts = ownTexts(u), total = 0;
    for (var i = 0; i < ts.length; i++) {
      var t = ts[i], len = t.data.length;
      if (o <= total + len) {
        var k = o - total, ref;
        if (k <= 0) { t.parentNode.insertBefore(node, t); return; }
        if (k >= len) {
          ref = t;
          // at the end of a highlight or search mark: sit after the mark, not inside its color
          while (!ref.nextSibling && ref.parentNode && ref.parentNode.matches && ref.parentNode.matches("mark.user-hl, mark.search-hit, mark.shared-hl")) ref = ref.parentNode;
          ref.parentNode.insertBefore(node, ref.nextSibling);
          return;
        }
        var rest = t.splitText(k);
        rest.parentNode.insertBefore(node, rest);
        return;
      }
      total += len;
    }
    u.appendChild(node);
  }
  function anchorFor(u, o) {
    var t = unitText(u);
    return { u: unitKey(u), o: o, b: t.slice(Math.max(0, o - NOTE_CTX), o), a: t.slice(o, o + NOTE_CTX) };
  }
  // where a saved note goes now: its unit and offset if the words around it still match, else the
  // same words elsewhere in that unit, else anywhere in the guide (if they occur exactly once), else
  // its old unit and offset. Null only when its unit is gone and its words are nowhere.
  function resolveNote(n) {
    var u = unitByKey(n.u), b = n.b || "", a = n.a || "", ctx = b + a;
    if (u) {
      var t = unitText(u), o = Math.min(Math.max(0, n.o || 0), t.length);
      if (t.slice(o - b.length, o) === b && t.slice(o, o + a.length) === a) return { u: u, o: o };
      if (ctx.replace(/\s+/g, "").length >= 4) {
        var at = nearestIndex(t, ctx, o - b.length);
        if (at >= 0) return { u: u, o: at + b.length };
      }
    }
    if (ctx.replace(/\s+/g, "").length >= 8) {
      var hit = null, count = 0;
      ordered().forEach(function (x) {
        if (count > 1) return;
        var tx = unitText(x), i = tx.indexOf(ctx);
        while (i >= 0 && count < 2) { count++; hit = { u: x, o: i + b.length }; i = tx.indexOf(ctx, i + 1); }
      });
      if (count === 1) return hit;
    }
    if (u) return { u: u, o: Math.min(Math.max(0, n.o || 0), unitText(u).length) };
    return null;
  }
  var orphanNotes = [];
  (function () {
    var list = loadNotes();
    list.forEach(function (n) {
      if (!n || !n.id || !n.t) return;
      var pos = resolveNote(n);
      if (!pos) { orphanNotes.push(n); return; }
      insertAt(pos.u, pos.o, makeHost(n));
    });
  })();

  function saveNoteText(id, text, pending) {
    var list = loadNotes(), now = new Date().toISOString(), hit = false;
    list.forEach(function (n) { if (n.id === id) { n.t = text; n.m = now; hit = true; } });
    if (!hit && pending) { pending.t = text; pending.m = now; list.push(pending); hit = true; }
    if (!hit) return false;
    var ok = saveNotes(list);
    var h = hostOf(id);
    if (h) setHostText(h, text);
    pipNoteChanged(id, text);
    return ok;
  }
  // Deletes a note and its review item. Returns what Undo needs: the stored record, the exact spot the
  // box sat at (unit + offset, read from the page before it goes), and a promise of the removed review
  // item ({slug, item} or null).
  function deleteNote(id) {
    var h = hostOf(id), spot = null;
    if (h) {
      var u = findUnit(h.parentNode);
      if (u) { var r = document.createRange(); r.setStartBefore(h); spot = { u: u, o: offsetIn(u, r.startContainer, r.startOffset) }; }
      h.remove();
    }
    var list = loadNotes(), rec = null;
    list.forEach(function (n) { if (n.id === id) rec = n; });
    if (rec) saveNotes(list.filter(function (n) { return n.id !== id; }), [id]);
    return { rec: rec, spot: spot, item: pipNoteChanged(id, null) };
  }
  // Undo (2026-10-15): the note back at its exact spot with its stored anchor unchanged, stamped as the
  // newest change (so it outranks its own tombstone on every device), and its review item back with its
  // text, note and position. Returns the restored box (or null when the note had no spot on the page).
  function restoreNote(snap) {
    if (!snap || !snap.rec) return null;
    var rec = JSON.parse(JSON.stringify(snap.rec));
    rec.m = new Date().toISOString();
    var list = loadNotes().filter(function (n) { return n.id !== rec.id; });
    list.push(rec);
    if (!saveNotes(list)) return null;
    var h = null;
    if (!hostOf(rec.id)) {
      if (snap.spot && snap.spot.u.isConnected) {
        h = makeHost(rec);
        insertAt(snap.spot.u, Math.min(snap.spot.o, unitText(snap.spot.u).length), h);
      } else {
        orphanNotes = orphanNotes.filter(function (n) { return n.id !== rec.id; }).concat([rec]);
      }
    }
    if (snap.item && snap.item.then) snap.item.then(function (it) { if (it && window.PipReview) window.PipReview.add(it.slug, it.item); });
    return h;
  }
  // "Note deleted" with Undo for about 6 seconds. From the keyboard, focus goes to Undo (the control that
  // was used has just gone) and, when the toast leaves, back to the paragraph the note was in.
  // noFocus: the delete came from committing an emptied note (clicking or tabbing away), so the student
  // is already moving on; focus stays where they took it
  function noteDeletedToast(snap, noFocus) {
    if (!window.showToast) return;
    if (!snap || !snap.rec) { window.showToast("Note deleted", 2500); return; }
    var spotEl = snap.spot && snap.spot.u;
    window.showToast("Note deleted", 6000, {
      label: "Undo",
      focus: !noFocus && lastInput === "key",
      returnFocus: function () {
        var c = hlPanelOverlay && hlPanelOverlay.querySelector(".hl-panel-close");
        if (c) { try { c.focus({ preventScroll: true }); } catch (e) {} } else focusSpot(spotEl);
      },
      onClick: function (e) {
        var h = restoreNote(snap);
        if (hlPanelOverlay) openHlPanel();
        else if (h) {
          revealEl(h);
          if (e && e.detail === 0) { try { h.focus({ preventScroll: true }); } catch (x) {} }
        }
        window.showToast(h || !snap.spot ? "Note restored" : "Note restored to your notes list", 2500);
      }
    });
  }
  // Focus a spot in the text that is not normally focusable (a paragraph, a mark) for a keyboard user,
  // so Tab carries on from there; the temporary tabindex goes again when focus leaves.
  function focusSpot(el) {
    if (!el || !el.isConnected) return;
    if (!el.hasAttribute("tabindex")) {
      el.setAttribute("tabindex", "-1");
      el.setAttribute("data-hl-tmpfocus", "");
      el.addEventListener("blur", function off() {
        el.removeEventListener("blur", off);
        if (el.hasAttribute("data-hl-tmpfocus")) { el.removeAttribute("data-hl-tmpfocus"); el.removeAttribute("tabindex"); }
      });
    }
    try { el.focus({ preventScroll: true }); } catch (e) {}
  }
  // the last input was a key (Undo and the selection toolbar move focus only for keyboard users)
  var lastInput = "pointer";
  document.addEventListener("keydown", function () { lastInput = "key"; }, true);
  function revealEl(el) {
    for (var d = el.closest("details"); d; d = d.parentElement && d.parentElement.closest("details")) d.open = true;
    var panel = el.closest(".subj-panel");
    if (panel && !panel.classList.contains("active")) {
      var subj = panel.getAttribute("data-subj");
      var tab = Array.prototype.filter.call(document.querySelectorAll(".subj-tab"), function (t) { return t.dataset.subj === subj; })[0];
      if (tab) tab.click();
    }
  }
  // Where a new note goes (2026-10-15): the END OF THE SENTENCE that holds the spot, because a box pinned
  // at the clicked word broke the sentence for reading. A sentence ends at . ! ? or ; (plus any closing
  // quote or bracket) followed by a space or the end of the unit's text. A period is not an end after
  // "e.g.", "i.e.", "vs." and the like, inside a decimal (1.5), after an initial (E. coli, J. R.), or
  // when the next word starts with a small letter. No end after the spot: the end of the unit's text.
  // Notes saved before this keep their stored spot.
  var NOT_END = /(?:^|[\s(\[{“‘"'\/-])(?:[Ee]\.[Gg]|[Ii]\.[Ee]|[Vv]s|[Cc]f|[Ee]tc|[Aa]pprox|[Ee]sp|[Ii]ncl|Dr|Drs|Mr|Mrs|Ms|Prof|Sr|Jr|Fig|Figs|[Aa]l|U\.S|[ap]\.m|[A-Z]\.\s?[A-Z])$/;
  function sentenceEnd(t, o) {
    for (var i = Math.max(0, o - 1); i < t.length; i++) {
      var ch = t[i];
      if (ch !== "." && ch !== "!" && ch !== "?" && ch !== ";") continue;
      var j = i + 1;
      while (j < t.length && /["'”’»)\]}]/.test(t[j])) j++;
      if (j < t.length && !/\s/.test(t[j])) continue;               // 1.5, U.S, "e.g.,"
      if (ch === ".") {
        if (NOT_END.test(t.slice(Math.max(0, i - 12), i))) continue;
        var nx = t.slice(j, j + 8);
        if (/^\s*[a-z]/.test(nx)) continue;                          // E. coli, "approx. the"
        if (/(?:^|\s)[A-Z]$/.test(t.slice(Math.max(0, i - 2), i)) && /^\s*[A-Z]\.(?:\s|$)/.test(nx)) continue;   // J. R. Smith
      }
      return j;
    }
    return t.replace(/\s+$/, "").length;
  }
  function startNote(u, o) {
    var t = unitText(u);
    o = sentenceEnd(t, Math.min(Math.max(0, o), t.length));
    var n = anchorFor(u, o);
    n.id = newId("n"); n.t = ""; n.at = new Date().toISOString();
    var h = makeHost(n);
    insertAt(u, o, h);
    revealEl(h);
    openNoteEditor(n.id, n);
  }

  /* ------------------------------------------------------------------------------------------------
     Add to Pip (2026-10-11, finished 2026-10-15). See window.PipReview above. The saved bit is the
     guide's own words; the only other text is the student's own note.
     ------------------------------------------------------------------------------------------------ */
  var PIP_BASE = (function () {
    var sc = document.querySelector('script[src$="theme.js"]');
    return sc && sc.src ? sc.src.replace(/theme\.js(\?.*)?$/, "") : "";
  })();
  var PIP_PATH = (function () { try { return decodeURIComponent(location.pathname); } catch (e) { return location.pathname; } })().split("/").filter(Boolean);
  var PIP_FILE = PIP_PATH[PIP_PATH.length - 1] || "", PIP_FOLDER = PIP_PATH[PIP_PATH.length - 2] || "";
  var pipExam = null, pipExamPending = null;  // the Semester 2 exam this page belongs to ({s, f, t}), or false
  function pipExamP() {
    if (pipExam !== null) return Promise.resolve(pipExam);
    if (!window.PipReview || !PIP_BASE || !window.fetch || !PIP_FOLDER) return Promise.resolve((pipExam = false));
    if (pipExamPending) return pipExamPending;
    pipExamPending = fetch(PIP_BASE + "pip/data/index.json").then(function (r) { return r.ok ? r.json() : null; }).then(function (ix) {
      var hit = null;
      ((ix && ix.folders) || []).forEach(function (f) { if (f.f === PIP_FOLDER) hit = f; });
      pipExamPending = null;
      return (pipExam = hit ? { s: hit.s, f: hit.f, t: hit.t } : false);
    }).catch(function () { pipExamPending = null; return false; });   // not cached: a failed fetch may work next time
    return pipExamPending;
  }
  // Where a passage sits, the way tools/build_pip_data.py indexes the guide: `a` is the last element
  // with an id at or before it (so Pip's explanation cards and the quiz questions linked to that spot
  // line up), `st` the last h2/h3 before it, `k`/`kt` the enclosing section[id] and its heading.
  function sectionInfo(u) {
    var a = "", st = "", w = document.createTreeWalker(wrap, NodeFilter.SHOW_ELEMENT, null);
    w.currentNode = u;
    for (var el = u; el; el = w.previousNode()) {
      if (!a && el.id) a = el.id;
      if (!st && /^H[23]$/.test(el.tagName)) st = norm0(el.textContent);
      if (a && st) break;
    }
    var deck = u.closest("section[id]"), dh = deck && deck.querySelector("h1, h2, h3");
    return { a: a, st: st, k: deck ? deck.id : "", kt: dh ? norm0(dh.textContent) : "" };
  }
  function pipItem(u, text, note, extra) {
    var sec = sectionInfo(u), t = window.PipReview.trim(text);
    var it = { id: window.PipReview.idOf(t, PIP_FILE), f: PIP_FOLDER, d: PIP_FILE, a: sec.a, st: sec.st, k: sec.k, kt: sec.kt,
               u: ordered().indexOf(u), t: t, n: String(note || "").trim().slice(0, NOTE_MAX), at: new Date().toISOString() };
    if (extra) for (var f in extra) it[f] = extra[f];
    return it;
  }
  function pipToast(r, n) {
    if (!window.showToast) return;
    window.showToast(r === "added" ? "Added to your review guide (" + n + " saved). Find it from Pip or the home page."
      : r === "exists" ? "Already in your review guide (" + n + " saved)"
      : r === "removed" ? "Removed from your review guide (" + n + " saved)"
      : "Could not save here. Check that this browser allows site storage.", 3500);
  }
  function pipAdd(item) {
    return pipExamP().then(function (ex) {
      if (!ex || !item || !item.t) return null;
      var r = window.PipReview.add(ex.s, item);
      pipToast(r, window.PipReview.count(ex.s));
      return r;
    });
  }
  // "Ask Pip" (Jaxon, 2026-10-18: "Ask Pip about that..."): Pip's window opens on the question of what the
  // selected words mean. A few words become "What does “X” mean?", which is his definition path; a longer passage
  // becomes "Explain this: “…”". He answers the way he answers a typed question (the guides, and Claude reading
  // this exam's whole guide for a student who can use it). Pip lives on pa-quizzes.com only, and the group-study
  // pages keep him out, so the button shows only where window.__pip can take the question.
  function pipCanAsk() { return !!(window.__pip && window.__pip.ask && !window.__pip.gated); }
  function pipQuestion(t) {
    t = norm0(t).replace(/^[\s"“”'‘’(\[]+|[\s"“”'‘’)\],;:]+$/g, "");
    if (t.length > 400) t = t.slice(0, 400).replace(/\s+\S*$/, "") + "…";   // the helper takes 500 characters
    var term = t.replace(/[.!?]+$/, "");
    if (!term) return "";
    return term.split(" ").length <= 4 ? "What does “" + term + "” mean?" : "Explain this: “" + t + "”";
  }
  function pipAsk(text) { var q = pipQuestion(text); if (q && pipCanAsk()) window.__pip.ask(q); }
  // the same button inside a highlight's popover: the highlight's words
  function pipAskBtn(parent, textFn) {
    if (!pipCanAsk()) return;
    var b = document.createElement("button");
    b.type = "button"; b.className = "hl-note-btn hl-note-pip"; b.hidden = true;
    b.textContent = "Ask Pip"; b.title = "Ask Pip what this means";
    parent.appendChild(b);
    pipExamP().then(function (ex) {
      if (!ex || !b.isConnected) return;
      b.hidden = false;
      clampToViewport(parent);                    // one more button: keep the popover on screen
      b.addEventListener("click", function () { var t = textFn(); closePopover("done"); pipAsk(t); });
    });
  }
  // a Pip toggle button for a popover: label follows whether `idFn()` is in the list
  function pipToggle(parent, idFn, makeItem) {
    var b = document.createElement("button");
    b.type = "button"; b.className = "hl-note-btn hl-note-pip"; b.hidden = true;
    parent.appendChild(b);
    pipExamP().then(function (ex) {
      if (!ex || !b.isConnected) return;
      function label() {
        var on = window.PipReview.has(ex.s, idFn());
        b.textContent = on ? "Remove from Pip" : "Add to Pip";
        b.title = on ? "Take this out of your review guide" : "Save this to your review guide (My Review Guide)";
      }
      label(); b.hidden = false;
      b.addEventListener("click", function () {
        var id = idFn();
        if (window.PipReview.has(ex.s, id)) {
          window.PipReview.remove(ex.s, id);
          pipToast("removed", window.PipReview.count(ex.s));
          label();
        } else {
          var it = makeItem();
          if (!it) return;
          pipAdd(it).then(label);
        }
      });
    });
    return b;
  }
  function hlItem(key, note) {
    var recs = recsOf(key);
    if (!recs.length) return null;
    var pl = placeRec(recs[0]);
    return pl ? pipItem(pl.u, textOfRecs(recs), note, { o: pl.start }) : null;
  }
  function hlPipId(key) { return window.PipReview.idOf(window.PipReview.trim(textOfRecs(recsOf(key))), PIP_FILE); }
  // A text-box note in the review guide: the guide's own sentence around the spot, plus the note.
  function noteContext(u, o) {
    var t = unitText(u), s = o, e = o;
    while (s > 0 && !/[.!?;:]\s/.test(t.slice(s - 2, s))) s--;
    while (e < t.length && !/[.!?;:](\s|$)/.test(t.slice(e - 1, e + 1))) e++;
    var c = norm0(t.slice(s, Math.min(t.length, e + 1)));
    return c || norm0(t);
  }
  function noteItem(id, text) {
    var h = hostOf(id);
    if (!h || !text) return null;
    var u = findUnit(h.parentNode) || null;
    if (!u) return null;
    var r = document.createRange(); r.setStartBefore(h);
    var o = offsetIn(u, r.startContainer, r.startOffset);
    var it = pipItem(u, noteContext(u, o), text, { nid: id, o: o });
    it.id = "n:" + id;
    return it;
  }
  // A note's text changed (text) or the note was deleted (null): keep its review item in step. Returns a
  // promise of the removed item {slug, item} on a delete (for Undo), else of null.
  function pipNoteChanged(id, text) {
    function apply(ex) {
      if (!ex || !window.PipReview) return null;
      var s = ex.s, rid = "n:" + id, it = null;
      window.PipReview.load(s).forEach(function (x) { if (x.id === rid) it = x; });
      if (!it) return null;
      if (text === null) { window.PipReview.remove(s, rid); return { slug: s, item: it }; }
      window.PipReview.setNote(s, rid, text);
      return null;
    }
    if (!window.PipReview) return Promise.resolve(null);
    if (pipExam !== null) return Promise.resolve(apply(pipExam));     // known: change it now
    return pipExamP().then(apply);
  }

  /* ------------------------------------------------------------------------------------------------
     POPOVERS: one at a time. "commit" (clicking elsewhere) keeps what was typed; Escape cancels.
     ------------------------------------------------------------------------------------------------ */
  var pop = null;
  function closePopover(how) {
    if (!pop) return;
    var p = pop; pop = null;
    try { if (how === "cancel") { if (p.cancel) p.cancel(); } else if (how !== "silent" && p.commit) p.commit(); } catch (e) {}
    p.el.remove();
    if ((how === "cancel" || how === "done") && p.back) {
      if (typeof p.back === "function") { try { p.back(); } catch (e) {} }
      else if (p.back.isConnected) { try { p.back.focus({ preventScroll: true }); } catch (e) {} }
    }
  }
  function placePopover(el, anchor) {
    var rect = anchor.getBoundingClientRect();
    el.style.top = (rect.bottom + window.scrollY + 6) + "px";
    el.style.left = Math.max(8, rect.left + window.scrollX) + "px";
    document.body.appendChild(el);
    clampToViewport(el);
  }
  // Keep a floating panel inside the viewport. Called after the element is appended (so its real
  // size is known) with the desired top/left already set; nudges them back into bounds if needed.
  function clampToViewport(el) {
    var pad = 8;
    var rect = el.getBoundingClientRect();
    var left = rect.left, top = rect.top;
    if (rect.right > window.innerWidth - pad) left -= (rect.right - (window.innerWidth - pad));
    if (left < pad) left = pad;
    if (rect.bottom > window.innerHeight - pad) top -= (rect.bottom - (window.innerHeight - pad));
    if (top < pad) top = pad;
    el.style.left = (left + window.scrollX) + "px";
    el.style.top = (top + window.scrollY) + "px";
  }
  function popBtn(cls, text, fn) {
    var b = document.createElement("button");
    b.type = "button"; b.className = "hl-note-btn " + cls; b.textContent = text;
    b.addEventListener("click", fn);
    return b;
  }

  function openHlPopover(key, anchor, back) {
    hideToolbar();
    closePopover("commit");
    var recs = recsOf(key);
    if (!recs.length) return;
    var el = document.createElement("div");
    el.className = "hl-note-popover";
    el.setAttribute("role", "dialog");
    el.setAttribute("aria-label", "Highlight options");
    var current = recs[0].color || "yellow", saved = recs[0].note || "";

    // Recolor without deleting and reapplying; the current color gets a ring.
    var colorRow = document.createElement("div");
    colorRow.className = "hl-note-colors";
    COLORS.forEach(function (color) {
      var b = document.createElement("button");
      b.type = "button";
      b.className = "hl-swatch hl-swatch-" + color + (color === current ? " hl-swatch-current" : "");
      b.setAttribute("aria-label", "Change to " + color);
      b.setAttribute("aria-pressed", color === current ? "true" : "false");
      b.addEventListener("click", function () {
        marksOf(key).forEach(function (m) {
          COLORS.forEach(function (c) { m.classList.remove("user-hl-" + c); });
          m.classList.add("user-hl-" + color);
        });
        updateRecs(key, { color: color });
        colorRow.querySelectorAll(".hl-swatch").forEach(function (sw) { sw.classList.remove("hl-swatch-current"); sw.setAttribute("aria-pressed", "false"); });
        b.classList.add("hl-swatch-current"); b.setAttribute("aria-pressed", "true");
      });
      colorRow.appendChild(b);
    });
    el.appendChild(colorRow);

    var textarea = document.createElement("textarea");
    textarea.className = "hl-note-textarea";
    textarea.placeholder = "Add a note about this passage… (⌘/Ctrl+Enter to save)";
    textarea.setAttribute("aria-label", "Note about this highlight");
    textarea.maxLength = NOTE_MAX;
    textarea.value = saved;
    el.appendChild(textarea);

    function commit() {
      var note = textarea.value.trim();
      if (note === saved) return;
      saved = note;
      setMarksNote(key, note);
      updateRecs(key, { note: note });
      pipExamP().then(function (ex) { if (ex) window.PipReview.setNote(ex.s, hlPipId(key), note); });
    }
    var row = document.createElement("div");
    row.className = "hl-note-row";
    row.appendChild(popBtn("hl-note-remove", "Remove highlight", function () {
      removeHighlight(key);
      closePopover("silent");
    }));
    row.appendChild(popBtn("hl-note-save", "Save note", function () { closePopover("done"); }));
    el.appendChild(row);
    textarea.addEventListener("keydown", function (e) {
      if ((e.metaKey || e.ctrlKey) && e.key === "Enter") { e.preventDefault(); closePopover("done"); }
    });
    // "Add to Pip" (a toggle: "Remove from Pip" once the passage is in the review guide)
    pipToggle(el, function () { return hlPipId(key); }, function () { return hlItem(key, textarea.value.trim()); });
    pipAskBtn(el, function () { return textOfRecs(recsOf(key)); });

    pop = { el: el, commit: commit, flush: commit, back: back || null };
    placePopover(el, anchor);
    textarea.focus({ preventScroll: true });
  }

  function openNoteEditor(id, pending) {
    hideToolbar();
    closePopover("commit");
    var h = hostOf(id), rec = pending || noteRec(id);
    if (!h || !rec) return;
    var el = document.createElement("div");
    el.className = "hl-note-popover gnote-editor";
    el.setAttribute("role", "dialog");
    el.setAttribute("aria-label", pending ? "New note" : "Edit your note");
    var head = document.createElement("div");
    head.className = "gnote-editor-head";
    head.textContent = pending ? "New note" : "Your note";
    el.appendChild(head);
    var textarea = document.createElement("textarea");
    textarea.className = "hl-note-textarea";
    textarea.placeholder = "Type your note… (⌘/Ctrl+Enter to save)";
    textarea.setAttribute("aria-label", "Your note");
    textarea.maxLength = NOTE_MAX;
    textarea.value = rec.t || "";
    el.appendChild(textarea);
    var saved = rec.t || "", isNew = !!pending;
    function commit() {
      var v = textarea.value.trim();
      if (!v) {
        if (isNew) { var hh = hostOf(id); if (hh) hh.remove(); }
        else noteDeletedToast(deleteNote(id), true);
        return;
      }
      if (v === saved && !isNew) return;
      if (saveNoteText(id, v, isNew ? pending : null)) { saved = v; isNew = false; }
    }
    function cancel() {
      if (isNew) { var hh = hostOf(id); if (hh) hh.remove(); }
    }
    var row = document.createElement("div");
    row.className = "hl-note-row";
    row.appendChild(popBtn("hl-note-remove", isNew ? "Cancel" : "Delete note", function () {
      if (isNew) { closePopover("cancel"); return; }
      pop.commit = null; pop.back = null;
      var snap = deleteNote(id);
      closePopover("silent");
      noteDeletedToast(snap);
    }));
    row.appendChild(popBtn("hl-note-save", "Save note", function () { closePopover("done"); }));
    el.appendChild(row);
    textarea.addEventListener("keydown", function (e) {
      if ((e.metaKey || e.ctrlKey) && e.key === "Enter") { e.preventDefault(); closePopover("done"); }
    });
    // Add to Pip: the guide's sentence around the note, with the note as "your note"
    pipToggle(el, function () { return "n:" + id; }, function () {
      var v = textarea.value.trim();
      if (!v) { if (window.showToast) window.showToast("Type your note first", 2500); return null; }
      if (v !== saved || isNew) { if (saveNoteText(id, v, isNew ? pending : null)) { saved = v; isNew = false; } }
      return noteItem(id, v);
    });
    function flush() {
      var v = textarea.value.trim();
      if (v && (v !== saved || isNew) && saveNoteText(id, v, isNew ? pending : null)) { saved = v; isNew = false; }
    }
    pop = { el: el, commit: commit, cancel: cancel, flush: flush, back: h };
    placePopover(el, h);
    textarea.focus({ preventScroll: true });
  }

  /* ------------------------------------------------------------------------------------------------
     SELECTION TOOLBAR: color swatches, "Note" and (on a Semester 2 exam's pages) "Add to Pip".
     Keyboard (2026-10-15), the WAI-ARIA toolbar pattern: after a selection made with the keyboard
     (Shift + arrows with caret browsing, or select-all), a polite live region says how to reach it;
     nothing takes focus by itself, so someone just reading is never pulled away. Tab, while the
     selection is there, moves into the toolbar (one tab stop); the arrow keys, Home and End move
     between its buttons; Escape closes it and puts focus and the selection back where they were; Tab
     again leaves it and carries on from the selection.
     ------------------------------------------------------------------------------------------------ */
  var toolbar = null, lastPointer = "mouse", tbBack = null, liveEl = null;
  function hideToolbar() { if (toolbar) { toolbar.remove(); toolbar = null; } }
  function announce(msg) {
    if (!liveEl) {
      liveEl = document.createElement("div");
      liveEl.className = "sr-only";
      liveEl.setAttribute("role", "status");
      liveEl.setAttribute("aria-live", "polite");
      document.body.appendChild(liveEl);
    }
    liveEl.textContent = "";
    setTimeout(function () { if (liveEl) liveEl.textContent = msg; }, 60);
  }
  function tbButtons(bar) { return Array.prototype.slice.call(bar.querySelectorAll("button")); }
  function tbFocus(bar, i) {
    var bs = tbButtons(bar);
    if (!bs.length) return;
    i = (i + bs.length) % bs.length;
    bs.forEach(function (b, k) { b.tabIndex = k === i ? 0 : -1; });
    try { bs[i].focus({ preventScroll: true }); } catch (e) {}
  }
  // where focus goes when the toolbar is left from the keyboard: the element that had it, else the
  // unit the selection ended in (made focusable for the moment, see focusSpot)
  function tbReturn(reselect) {
    var back = tbBack;
    tbBack = null;
    if (!back) return;
    var el = back.el;
    if (el && el !== document.body && el !== document.documentElement && el.isConnected && !(toolbar && toolbar.contains(el))) {
      try { el.focus({ preventScroll: true }); } catch (e) {}
    } else {
      focusSpot(findUnit(back.range.endContainer) || findUnit(back.range.startContainer));
    }
    if (reselect) { try { var s = window.getSelection(); s.removeAllRanges(); s.addRange(back.range); } catch (e) {} }
  }
  function tbBtn(cls, text, label, fn) {
    var b = document.createElement("button");
    b.type = "button"; b.className = cls;
    if (text) b.textContent = text;
    b.setAttribute("aria-label", label); b.title = label;
    b.tabIndex = -1;
    // mousedown is swallowed so the text selection survives the click; the action runs on click,
    // which a keyboard (Enter / Space) also fires
    b.addEventListener("mousedown", function (e) { e.preventDefault(); e.stopPropagation(); });
    b.addEventListener("click", function (e) { e.preventDefault(); e.stopPropagation(); fn(e); });
    return b;
  }
  function showToolbar(range, viaKey) {
    var again = !!(toolbar && toolbar.__kbd && viaKey);   // the same keyboard selection growing: say it once
    hideToolbar();
    var saved = range.cloneRange(), rect = range.getBoundingClientRect();
    var touch = lastPointer === "touch" || lastPointer === "pen";
    var bar = document.createElement("div");
    bar.className = "hl-toolbar";
    bar.setAttribute("role", "toolbar");
    bar.setAttribute("aria-label", "Highlight tools");
    bar.__kbd = !!viaKey;
    function fromKeys() { return toolbar === bar && bar.contains(document.activeElement); }
    COLORS.forEach(function (color) {
      bar.appendChild(tbBtn("hl-swatch hl-swatch-" + color, "", "Highlight " + color, function () {
        var kb = fromKeys(), back = tbBack;
        tbBack = null;
        var key = createHighlight(saved, color);
        window.getSelection().removeAllRanges();
        hideToolbar();
        if (!key) {
          if (kb) { tbBack = back; tbReturn(true); }
          if (window.showToast) window.showToast("That part of the guide can't be highlighted.", 3000);
          return;
        }
        // Prompt for an optional note right away -- annotating is meant to feel like one motion with
        // highlighting. Clicking away keeps the highlight (and anything typed).
        var ms = marksOf(key);
        if (ms.length) openHlPopover(key, ms[ms.length - 1], kb ? function () { focusSpot(marksOf(key).pop()); } : null);
      }));
    });
    bar.appendChild(tbBtn("hl-tbtext", "Note", "Add a note box here", function () {
      var runs = snapRuns(runsFrom(saved).filter(Boolean));
      tbBack = null;
      window.getSelection().removeAllRanges();
      hideToolbar();
      if (!runs.length) return;
      var last = runs[runs.length - 1];
      startNote(last.u, last.end);
    }));
    bar.firstChild.tabIndex = 0;
    bar.addEventListener("keydown", function (e) {
      var bs = tbButtons(bar), i = bs.indexOf(document.activeElement);
      if (e.key === "ArrowRight" || e.key === "ArrowDown") { e.preventDefault(); tbFocus(bar, i + 1); }
      else if (e.key === "ArrowLeft" || e.key === "ArrowUp") { e.preventDefault(); tbFocus(bar, i - 1); }
      else if (e.key === "Home") { e.preventDefault(); tbFocus(bar, 0); }
      else if (e.key === "End") { e.preventDefault(); tbFocus(bar, bs.length - 1); }
      else if (e.key === "Escape" || e.key === "Esc") { e.preventDefault(); e.stopPropagation(); hideToolbar(); tbReturn(true); }
      // Tab leaves the toolbar: focus goes back to the selection and the browser moves on from there
      else if (e.key === "Tab") { e.stopPropagation(); hideToolbar(); tbReturn(false); }
    });
    // If the drag ends below the toolbar's spot, a phone's own copy/paste menu sits above the
    // selection, so on touch the toolbar goes underneath instead.
    bar.style.top = (touch ? rect.bottom + window.scrollY + 12 : rect.top + window.scrollY - 46) + "px";
    bar.style.left = Math.max(8, rect.left + window.scrollX) + "px";
    document.body.appendChild(bar);
    clampToViewport(bar);
    toolbar = bar;
    if (viaKey && !again) announce("Highlight tools are open for your selection. Press Tab to use them, or Escape to close them.");
    pipExamP().then(function (ex) {
      if (!ex || toolbar !== bar) return;
      bar.appendChild(tbBtn("hl-tbtext hl-pipbtn", "Add to Pip", "Add to Pip: save this to your review guide", function () {
        var kb = fromKeys();
        var runs = snapRuns(runsFrom(saved).filter(Boolean));
        hideToolbar();
        if (kb) tbReturn(false); else tbBack = null;
        window.getSelection().removeAllRanges();
        if (!runs.length) return;
        pipAdd(pipItem(runs[0].u, runsText(runs), "", { o: runs[0].start }));
      }));
      if (pipCanAsk()) bar.appendChild(tbBtn("hl-tbtext hl-pipbtn", "Ask Pip", "Ask Pip what this means", function () {
        // whole words, the way Add to Pip takes them (a drag from mid-word must not ask about "ypertension")
        var kb = fromKeys(), runs = snapRuns(runsFrom(saved).filter(Boolean));
        hideToolbar();
        if (kb) tbReturn(false); else tbBack = null;
        window.getSelection().removeAllRanges();
        if (runs.length) pipAsk(runsText(runs));
      }));
      clampToViewport(bar);
    });
  }
  // Tab with a live selection and the toolbar showing: into the toolbar (never from a form field or an
  // open note box, and not once the selection has collapsed, e.g. after a plain arrow key)
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Tab" || e.shiftKey || e.altKey || e.ctrlKey || e.metaKey || !toolbar) return;
    var a = document.activeElement;
    if (toolbar.contains(a) || (pop && pop.el.contains(a))) return;
    if (a && (/^(input|textarea|select)$/i.test(a.tagName) || a.isContentEditable)) return;
    var s = window.getSelection();
    if (!s || s.isCollapsed || !s.rangeCount || !s.toString().trim()) return;
    e.preventDefault();
    tbBack = { el: a, range: s.getRangeAt(0).cloneRange() };
    var bs = tbButtons(toolbar), cur = 0;
    bs.forEach(function (b, k) { if (b.tabIndex === 0) cur = k; });
    tbFocus(toolbar, cur);
  });

  function onSelectionDone(e, how) {
    how = how || {};
    if (e && e.target && e.target.closest) {
      if (toolbar && toolbar.contains(e.target)) return;
      if (pop && pop.el.contains(e.target)) return;
      if (e.target.closest(".gnote, input, textarea, select, .hl-panel-overlay")) return;
    }
    if (placing) return;
    var sel = window.getSelection();
    if (!sel || sel.isCollapsed || sel.rangeCount === 0 || !sel.toString().trim()) { hideToolbar(); return; }
    var range = sel.getRangeAt(0);
    var root = range.commonAncestorContainer;
    if (root.nodeType !== 1) root = root.parentNode;
    if (!root || !(wrap.contains(root) || root.contains(wrap))) { hideToolbar(); return; }
    var runs = runsFrom(range);
    if (runs.length && runs[runs.length - 1] === null) {
      hideToolbar();
      if (!how.quiet && window.showToast) window.showToast("That selection is too long to highlight. Select a smaller passage.", 3000);
      return;
    }
    if (!runs.length) {
      hideToolbar();
      // Nothing new to mark: either it is all highlighted already (click the highlight to change it;
      // no message) or it is text no highlight can hold (a button label, a picture's text).
      var hl = root.closest("mark.user-hl") || Array.prototype.some.call(wrap.querySelectorAll("mark.user-hl"), function (m) {
        try { return range.intersectsNode(m); } catch (x) { return false; }
      });
      if (!hl && !how.quiet && window.showToast) window.showToast("That part of the guide can't be highlighted.", 3000);
      return;
    }
    showToolbar(range, !!how.key);
  }
  document.addEventListener("pointerdown", function (e) { lastPointer = e.pointerType || "mouse"; lastInput = "pointer"; }, true);
  document.addEventListener("mouseup", function (e) {
    if (lastPointer === "touch" || lastPointer === "pen") return;   // touch: selectionchange below
    onSelectionDone(e);
  });
  // Phones and tablets fire no mouseup after a long-press selection, so the toolbar used to never
  // appear there. Wait for the selection handles to settle instead.
  var selTimer = null;
  document.addEventListener("selectionchange", function () {
    if (lastPointer !== "touch" && lastPointer !== "pen") return;
    clearTimeout(selTimer);
    selTimer = setTimeout(function () {
      var a = document.activeElement;
      if (a && /^(input|textarea|select)$/i.test(a.tagName)) return;
      onSelectionDone(null);
    }, 500);
  });
  // keyboard selection: Shift + arrows / Home / End / Page keys (with caret browsing), letting go of
  // Shift after them, or select-all (quiet: a whole-page select-all is too long and that is fine)
  var keySel = false;
  document.addEventListener("keydown", function (e) {
    if (!e.shiftKey || !/^(Arrow|Home|End|Page)/.test(e.key)) return;
    var t = e.target;      // Shift + arrows inside a text field selects in the field, not the guide
    keySel = !(t && t.nodeType === 1 && (/^(input|textarea|select)$/i.test(t.tagName) || t.isContentEditable));
  }, true);
  document.addEventListener("keyup", function (e) {
    var sel = keySel;
    if (e.key === "Shift") keySel = false;          // letting go of Shift ends the gesture, whatever returns below
    var a = document.activeElement;
    if (a && (/^(input|textarea|select)$/i.test(a.tagName) || a.isContentEditable)) return;
    if (toolbar && toolbar.contains(a)) return;
    if (pop && pop.el.contains(a)) return;
    var nav = /^(Arrow|Home|End|Page)/.test(e.key);
    if (nav && !e.shiftKey) {                       // the caret moved on: a collapsed selection has no tools
      var s = window.getSelection();
      if (toolbar && (!s || s.isCollapsed)) hideToolbar();
      return;
    }
    var all = (e.ctrlKey || e.metaKey) && (e.key === "a" || e.key === "A");
    if (!all && !(sel && ((e.shiftKey && nav) || e.key === "Shift"))) return;
    onSelectionDone(null, { key: true, quiet: all });
  });
  document.addEventListener("mousedown", function (e) {
    if (toolbar && !toolbar.contains(e.target)) hideToolbar();
    if (pop && !pop.el.contains(e.target)) closePopover("commit");
  });
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    hideToolbar();
    if (pop) closePopover("cancel");
    else if (placing) setPlacing(false);
    closeHlPanel();
  });
  window.addEventListener("pagehide", function () { if (pop) closePopover("commit"); });
  // An iPhone that sends the tab to the background fires no pagehide: keep what has been typed so far
  // (the editor stays open; an emptied box is not taken as "delete" here).
  document.addEventListener("visibilitychange", function () {
    if (document.visibilityState === "hidden" && pop && pop.flush) { try { pop.flush(); } catch (e) {} }
  });
  // Selecting words in an accordion's title by dragging ends in a click on the <summary>, which the
  // browser treats as "open/close": a drag that leaves a selection is not a toggle.
  document.addEventListener("click", function (e) {
    var sm = e.target && e.target.closest && e.target.closest("summary");
    if (!sm || !wrap.contains(sm)) return;
    var s = window.getSelection();
    if (s && !s.isCollapsed && s.toString().trim() && s.rangeCount && s.getRangeAt(0).intersectsNode(sm)) e.preventDefault();
  }, true);

  /* ------------------------------------------------------------------------------------------------
     "Add a note" tool: click it, then click the spot. Keyboard: Enter on the tool pins a note at the
     end of the paragraph you are reading (the first one fully below the toolbar).
     ------------------------------------------------------------------------------------------------ */
  var placing = false, noteBtn = null;
  function setPlacing(on) {
    placing = on;
    document.documentElement.classList.toggle("gnote-placing", on);
    if (noteBtn) noteBtn.setAttribute("aria-pressed", on ? "true" : "false");
    if (on && window.showToast) {
      var touch = lastPointer === "touch" || lastPointer === "pen";
      window.showToast((touch ? "Tap" : "Click") + " the spot in the guide where your note should go. Press Esc to cancel.", 4000);
    }
  }
  function caretAt(x, y) {
    var node = null, off = 0, p;
    try {
      if (document.caretPositionFromPoint) { p = document.caretPositionFromPoint(x, y); if (p) { node = p.offsetNode; off = p.offset; } }
      else if (document.caretRangeFromPoint) { p = document.caretRangeFromPoint(x, y); if (p) { node = p.startContainer; off = p.startOffset; } }
    } catch (e) {}
    return node ? { node: node, off: off } : null;
  }
  document.addEventListener("click", function (e) {
    if (!placing) return;
    if (noteBtn && noteBtn.contains(e.target)) return;
    if (!wrap.contains(e.target) || (e.target.closest && e.target.closest(".gnote"))) { setPlacing(false); return; }
    e.preventDefault(); e.stopPropagation();
    var c = caretAt(e.clientX, e.clientY), u = c && wrap.contains(c.node) ? findUnit(c.node) : null;
    if (!u) {
      if (window.showToast) window.showToast("Pick a spot in the text (not a picture or button). Press Esc to cancel.", 3500);
      return;
    }
    setPlacing(false);
    startNote(u, offsetIn(u, c.node, c.off));
  }, true);
  function noteAtReadingSpot() {
    var top = 60, list = ordered(), u = null;
    for (var i = 0; i < list.length; i++) {
      var r = list[i].getBoundingClientRect();
      if (!r.height || !list[i].getClientRects().length) continue;
      if (r.top >= top && r.bottom <= window.innerHeight) { u = list[i]; break; }
    }
    if (!u) { if (window.showToast) window.showToast("Scroll to the part of the guide you want, then try again.", 3000); return; }
    startNote(u, unitText(u).length);
  }

  // "Your highlights" review panel -- without this, a highlight/note is
  // effectively write-only: the only way to ever see it again is to
  // scroll back through the whole guide looking for colored marks. Reads
  // straight from the live <mark> elements and note boxes in the DOM so it
  // can never drift out of sync with what's actually on the page.
  var hlPanelOverlay = null;
  function closeHlPanel() { if (hlPanelOverlay) { hlPanelOverlay.remove(); hlPanelOverlay = null; } }
  function jumpTo(el) {
    closeHlPanel();
    revealEl(el);
    setTimeout(function () {
      el.scrollIntoView({ behavior: "smooth", block: "center" });
      el.classList.add("hl-flash");
      setTimeout(function () { el.classList.remove("hl-flash"); }, 1600);
    }, 30);
  }
  function openHlPanel() {
    closeHlPanel();
    hideToolbar();
    closePopover("commit");
    var keys = [], byKey = {};
    Array.prototype.forEach.call(wrap.querySelectorAll("mark.user-hl"), function (m) {
      var k = m.getAttribute("data-hlk");
      if (!byKey[k]) { byKey[k] = []; keys.push(k); }
      byKey[k].push(m);
    });
    var hosts = Array.prototype.slice.call(wrap.querySelectorAll(".gnote[data-gnote]")).filter(function (h) { return h.getAttribute("data-text"); });

    hlPanelOverlay = document.createElement("div");
    hlPanelOverlay.className = "hl-panel-overlay open";
    hlPanelOverlay.addEventListener("mousedown", function (e) {
      if (e.target === hlPanelOverlay) closeHlPanel();
    });

    var panel = document.createElement("div");
    panel.className = "hl-panel";
    panel.setAttribute("role", "dialog");
    panel.setAttribute("aria-label", "Your highlights and notes");

    var closeBtn = document.createElement("button");
    closeBtn.type = "button";
    closeBtn.className = "hl-panel-close";
    closeBtn.setAttribute("aria-label", "Close");
    closeBtn.innerHTML = "&times;";
    closeBtn.addEventListener("click", closeHlPanel);
    panel.appendChild(closeBtn);

    function item(swatchCls, excerptText, noteText, onJump, onDelete, delLabel) {
      var it = document.createElement("div");
      it.className = "hl-panel-item";
      var swatch = document.createElement("span");
      swatch.className = "hl-panel-swatch " + swatchCls;
      it.appendChild(swatch);
      var textWrap = document.createElement("div");
      textWrap.className = "hl-panel-text";
      if (excerptText) {
        var excerpt = document.createElement("p");
        excerpt.className = "hl-panel-excerpt";
        excerpt.textContent = "“" + excerptText + "”";
        textWrap.appendChild(excerpt);
      }
      if (noteText) {
        var note = document.createElement("p");
        note.className = "hl-panel-note";
        note.textContent = noteText;
        textWrap.appendChild(note);
      }
      it.appendChild(textWrap);
      var actions = document.createElement("div");
      actions.className = "hl-panel-actions";
      if (onJump) {
        var jumpBtn = document.createElement("button");
        jumpBtn.type = "button";
        jumpBtn.className = "hl-panel-jump";
        jumpBtn.textContent = "Jump to";
        jumpBtn.addEventListener("click", onJump);
        actions.appendChild(jumpBtn);
      }
      var delBtn = document.createElement("button");
      delBtn.type = "button";
      delBtn.className = "hl-panel-delete";
      delBtn.setAttribute("aria-label", delLabel);
      delBtn.innerHTML = "&times;";
      delBtn.addEventListener("click", onDelete);
      actions.appendChild(delBtn);
      it.appendChild(actions);
      return it;
    }

    var heading = document.createElement("h3");
    heading.textContent = "Your highlights" + (keys.length ? " (" + keys.length + ")" : "");
    panel.appendChild(heading);
    var list = document.createElement("div");          // one scroll area for highlights and notes
    list.className = "hl-panel-list";
    if (keys.length === 0) {
      var empty = document.createElement("p");
      empty.className = "hl-panel-empty";
      empty.textContent = "No highlights yet — select any text in this guide to add one.";
      list.appendChild(empty);
    }
    keys.forEach(function (k) {
      var ms = byKey[k], first = ms[0];
      var color = (first.className.match(/user-hl-(\w+)/) || [])[1] || "yellow";
      var text = norm0(ms.map(function (m) { return m.textContent; }).join(" "));
      list.appendChild(item("hl-swatch-" + color, text, first.dataset.note || "",
        function () { jumpTo(first); },
        function () { removeHighlight(k); openHlPanel(); }, "Delete this highlight"));
    });
    var nNotes = hosts.length + orphanNotes.length;
    var nh = document.createElement("h3");
    nh.className = "hl-panel-subhead";
    nh.textContent = "Your notes" + (nNotes ? " (" + nNotes + ")" : "");
    list.appendChild(nh);
    if (!nNotes) {
      var none = document.createElement("p");
      none.className = "hl-panel-empty";
      none.textContent = "No notes yet — use “Add a note” in the toolbar, then click the spot.";
      list.appendChild(none);
    }
    hosts.forEach(function (h) {
      var id = h.getAttribute("data-gnote");
      list.appendChild(item("gnote-swatch", "", h.getAttribute("data-text"),
        function () { jumpTo(h); setTimeout(function () { try { h.focus({ preventScroll: true }); } catch (e) {} }, 400); },
        function () { var snap = deleteNote(id); openHlPanel(); noteDeletedToast(snap); }, "Delete this note"));
    });
    orphanNotes.forEach(function (n) {
      list.appendChild(item("gnote-swatch", "", n.t + "  (its spot in the guide has changed)", null,
        function () {
          var snap = deleteNote(n.id);
          orphanNotes = orphanNotes.filter(function (x) { return x !== n; });
          openHlPanel(); noteDeletedToast(snap);
        }, "Delete this note"));
    });
    panel.appendChild(list);

    hlPanelOverlay.appendChild(panel);
    document.body.appendChild(hlPanelOverlay);
    closeBtn.focus({ preventScroll: true });
  }

  // In-guide search. Lives in this same closure (rather than a separate
  // IIFE) purely to reuse `wrap` -- otherwise unrelated to highlighting.
  // Walks every text node under `wrap` (not the highlight engine's `units`
  // list) because search needs to find matches inside table cells, IO-nav
  // pill labels, chip letters, everything -- not just the paragraph/list
  // granularity highlighting cares about. On the tabbed Anatomy Exam 3
  // guide, `.subj-panel`s the user hasn't clicked into are `display:none`
  // but still fully present in the DOM, so their text is found same as any
  // other guide's -- jumping to a match there re-uses the guide's own
  // `.subj-tab` click handler (see inline <script> at the bottom of that
  // file) to activate the right panel before scrolling, rather than
  // duplicating that panel-switching logic here.
  var searchMarks = [];
  var searchIndex = -1;

  function clearSearchMarks() {
    searchMarks.forEach(function (mark) {
      if (!mark.parentNode) return;
      var parent = mark.parentNode;
      while (mark.firstChild) parent.insertBefore(mark.firstChild, mark);
      parent.removeChild(mark);
      parent.normalize();
    });
    searchMarks = [];
    searchIndex = -1;
  }

  function runSearch(query) {
    clearSearchMarks();
    var q = query.trim().toLowerCase();
    if (q.length < 2) { updateSearchCount(); return; }

    // Collect text nodes first, then mutate -- splicing marks into the DOM
    // while a TreeWalker is still mid-walk over it is exactly the kind of
    // live-mutation-during-traversal bug that produces skipped/duplicated
    // nodes, so every node is gathered up front and only touched after.
    var walker = document.createTreeWalker(wrap, NodeFilter.SHOW_TEXT, {
      acceptNode: function (node) {
        return node.nodeValue && node.nodeValue.toLowerCase().indexOf(q) !== -1
          ? NodeFilter.FILTER_ACCEPT
          : NodeFilter.FILTER_REJECT;
      }
    });
    var textNodes = [];
    var n;
    while ((n = walker.nextNode())) textNodes.push(n);

    textNodes.forEach(function (node) {
      var text = node.nodeValue;
      var lower = text.toLowerCase();
      var frag = document.createDocumentFragment();
      var lastEnd = 0, pos;
      while ((pos = lower.indexOf(q, lastEnd)) !== -1) {
        if (pos > lastEnd) frag.appendChild(document.createTextNode(text.slice(lastEnd, pos)));
        var mark = document.createElement("mark");
        mark.className = "search-hit";
        mark.textContent = text.slice(pos, pos + q.length);
        frag.appendChild(mark);
        searchMarks.push(mark);
        lastEnd = pos + q.length;
      }
      if (lastEnd < text.length) frag.appendChild(document.createTextNode(text.slice(lastEnd)));
      node.parentNode.replaceChild(frag, node);
    });

    if (searchMarks.length) goToSearchMatch(0);
    else updateSearchCount();
  }

  function goToSearchMatch(i) {
    if (!searchMarks.length) return;
    if (searchIndex >= 0 && searchMarks[searchIndex]) {
      searchMarks[searchIndex].classList.remove("search-hit-current");
    }
    searchIndex = (i + searchMarks.length) % searchMarks.length;
    var mark = searchMarks[searchIndex];
    mark.classList.add("search-hit-current");

    var panel = mark.closest(".subj-panel");
    if (panel && !panel.classList.contains("active")) {
      var subj = panel.getAttribute("data-subj");
      var tab = Array.prototype.filter.call(
        document.querySelectorAll(".subj-tab"),
        function (t) { return t.dataset.subj === subj; }
      )[0];
      if (tab) tab.click();
    }

    mark.scrollIntoView({ behavior: "smooth", block: "center" });
    updateSearchCount();
  }

  var searchCountEl = null;
  function updateSearchCount() {
    if (!searchCountEl) return;
    searchCountEl.textContent = searchMarks.length
      ? (searchIndex + 1) + " / " + searchMarks.length
      : "0 / 0";
  }

  function initGuideSearch() {
    var backBar = document.querySelector(".guide-back-bar");
    if (!backBar || !backBar.parentNode) return null;

    var bar = document.createElement("div");
    bar.className = "guide-search-bar";
    bar.id = "guide-search-bar";
    bar.innerHTML =
      '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex:0 0 auto;opacity:.55"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>' +
      '<input type="text" class="guide-search-input" id="guide-search-input" placeholder="Search this guide…" autocomplete="off">' +
      '<span class="guide-search-count" id="guide-search-count"></span>' +
      '<button type="button" class="guide-search-nav" id="guide-search-prev" aria-label="Previous match" title="Previous match (Shift+Enter)">' +
        '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"/></svg>' +
      '</button>' +
      '<button type="button" class="guide-search-nav" id="guide-search-next" aria-label="Next match" title="Next match (Enter)">' +
        '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>' +
      '</button>' +
      '<button type="button" class="guide-search-close" id="guide-search-close" aria-label="Close search">&times;</button>';
    backBar.parentNode.insertBefore(bar, backBar.nextSibling);

    var input = bar.querySelector("#guide-search-input");
    searchCountEl = bar.querySelector("#guide-search-count");
    var prevBtn = bar.querySelector("#guide-search-prev");
    var nextBtn = bar.querySelector("#guide-search-next");
    var closeBtn = bar.querySelector("#guide-search-close");

    var debounceTimer = null;
    input.addEventListener("input", function () {
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(function () { runSearch(input.value); }, 150);
    });
    input.addEventListener("keydown", function (e) {
      if (e.key === "Enter") {
        e.preventDefault();
        if (e.shiftKey) goToSearchMatch(searchIndex - 1);
        else goToSearchMatch(searchIndex + 1);
      } else if (e.key === "Escape") {
        close();
      }
    });
    prevBtn.addEventListener("click", function () { goToSearchMatch(searchIndex - 1); });
    nextBtn.addEventListener("click", function () { goToSearchMatch(searchIndex + 1); });
    closeBtn.addEventListener("click", close);

    function isOpen() { return bar.classList.contains("open"); }
    function open() {
      bar.classList.add("open");
      input.focus();
    }
    function close() {
      bar.classList.remove("open");
      input.value = "";
      clearSearchMarks();
      updateSearchCount();
    }
    function toggle() { if (isOpen()) close(); else open(); }

    // "/" opens search from anywhere on the guide, same convention as
    // GitHub/Slack -- guides have no other single-key shortcut to collide
    // with (that's quiz-only, gated behind #timerpill, which no guide has).
    // Guarded against firing while any text input/textarea already has
    // focus (typing "/" into the highlight note textarea, for instance)
    // so it only ever acts as a global shortcut, never hijacks real typing.
    document.addEventListener("keydown", function (e) {
      if (e.key !== "/" || isOpen()) return;
      var active = document.activeElement;
      if (active && /^(input|textarea)$/i.test(active.tagName)) return;
      e.preventDefault();
      open();
    });

    return { toggle: toggle };
  }

  var guideSearchHelp = initGuideSearch();

  // Shared highlights (opt-in, added 2026-07-14). Broadcasts each
  // highlight's POSITION ONLY (idx/start/end + owning uid) to
  // sharedHighlights/{guideId}/marks/{uid_idx_start_end} in Firestore --
  // never the color or note text, which stay local-only even when this is
  // on (see firestore.rules and feedback_presence memory for the full
  // design and why this needed its own opt-in toggle, unlike "who's
  // studying now" presence which is automatic). Renders other opted-in
  // signed-in students' shared marks as a distinct, read-only dotted
  // overlay (mark.shared-hl, theme.css) -- never your own, which already
  // render through the normal user-hl system above.
  //
  // `sharedHl` is a plain mutable object (not reassigned wholesale) so that
  // applyHighlight()/removeHighlight() above -- defined and potentially
  // *called* long before Firebase finishes loading -- can safely read
  // `sharedHl.enabled`/`sharedHl.uid` at call time without needing to know
  // whether boot() below has run yet; before boot() ever runs, `enabled`
  // is simply false and both calls are no-ops.
  var sharedHl = {
    enabled: false,
    uid: null,
    pushDoc: function () {},
    deleteDoc: function () {}
  };
  (function () {
    var guideId = encodeURIComponent(location.pathname);
    var sharedMarksByDocId = {}; // Firestore doc id -> rendered <mark> element, so a later snapshot can cleanly clear exactly these and nothing else
    var unsubscribe = null;
    var hintShown = localStorage.getItem("sharedHlHintShown") === "1";

    function isSharingEnabled() { return localStorage.getItem("shareHighlights") === "1"; }
    function markId(uid, idx, start, end) { return uid + "_" + idx + "_" + start + "_" + end; }

    function clearSharedMarks() {
      Object.keys(sharedMarksByDocId).forEach(function (id) {
        sharedMarksByDocId[id].forEach(unwrap);
      });
      sharedMarksByDocId = {};
    }

    // Same text-node wrapping as the student's own highlights (one mark per text node), so a shared
    // mark never splits a <strong> or a table cell either. idx may be an extra unit ("x12").
    function renderSharedDoc(doc, data) {
      var unit = unitByKey(data.idx);
      if (!unit || typeof data.start !== "number" || typeof data.end !== "number") return; // guide changed since -- skip
      var marks = wrapText(unit, data.start, data.end, function () {
        var mark = document.createElement("mark");
        mark.className = "shared-hl";
        mark.title = "Also highlighted by another student";
        return mark;
      }, "mark.shared-hl");
      if (marks.length) sharedMarksByDocId[doc.id] = marks;
    }

    function subscribe(db, uid) {
      unsubscribe = db.collection("sharedHighlights").doc(guideId).collection("marks").onSnapshot(function (snap) {
        clearSharedMarks();
        var any = false;
        snap.forEach(function (doc) {
          var data = doc.data();
          if (!data || data.uid === uid) return; // your own highlights already show via the local user-hl system
          renderSharedDoc(doc, data);
          any = true;
        });
        if (any && !hintShown) {
          hintShown = true;
          localStorage.setItem("sharedHlHintShown", "1");
          if (window.showToast) window.showToast("The dotted marks are highlights other students made on this guide.", 5500);
        }
      }, function () { /* permission-denied before Firestore rules are published, or offline -- just stay empty, same as presence.js */ });
    }

    // both resolve to true when the write landed, false when it did not (never reject)
    function pushDoc(db, uid, idx, start, end) {
      try {
        return db.collection("sharedHighlights").doc(guideId).collection("marks").doc(markId(uid, idx, start, end))
          .set({ idx: idx, start: start, end: end, uid: uid, updatedAt: firebase.firestore.FieldValue.serverTimestamp() })
          .then(function () { return true; }, function () { return false; });
      } catch (e) { return Promise.resolve(false); }
    }
    function deleteDoc(db, uid, idx, start, end) {
      try {
        return db.collection("sharedHighlights").doc(guideId).collection("marks").doc(markId(uid, idx, start, end)).delete()
          .then(function () { return true; }, function () { return false; });
      } catch (e) { return Promise.resolve(false); }
    }

    // Backfill bookkeeping (2026-10-15). The backfill used to run on EVERY auth callback, which fires on
    // every page load (and again on any later auth change), so each guide visit by a sharing student
    // re-wrote one Firestore document per highlight. Now it runs at most once per signed-in account
    // per page load, and not at all when the set of highlight positions is the one this device last
    // sent completely: a device-only marker ("local:" keys are never synced) holds a hash of the
    // account and the positions. A new or removed highlight updates the marker once its own write
    // lands, so the next visit costs nothing.
    var SENT_KEY = "local:sharedHlSent:" + location.pathname;
    var backfilled = {}, inSync = false;
    function posList() {
      return loadHighlights().filter(function (h) {
        return h && (typeof h.idx === "number" || typeof h.idx === "string") && typeof h.start === "number" && typeof h.end === "number";
      });
    }
    function sig(uid) {
      var s = uid + "|" + posList().map(function (h) { return h.idx + "_" + h.start + "_" + h.end; }).sort().join(","), x = 0x811c9dc5;
      for (var i = 0; i < s.length; i++) { x ^= s.charCodeAt(i); x = Math.imul(x, 0x01000193); }
      return (x >>> 0).toString(36) + "." + s.length;
    }
    function markSent(uid) { try { localStorage.setItem(SENT_KEY, sig(uid)); } catch (e) {} }
    function backfill(db, uid) {
      if (backfilled[uid]) return;
      backfilled[uid] = true;
      var have = null;
      try { have = localStorage.getItem(SENT_KEY); } catch (e) {}
      if (have && have === sig(uid)) { inSync = true; return; }     // nothing changed since the last full send
      inSync = false;
      Promise.all(posList().map(function (h) { return pushDoc(db, uid, h.idx, h.start, h.end); })).then(function (r) {
        if (r.every(Boolean)) { inSync = true; markSent(uid); }
      });
    }

    function applyState(db, user) {
      var wantsSharing = isSharingEnabled();
      var signedIn = user && !user.isAnonymous;
      if (unsubscribe) { unsubscribe(); unsubscribe = null; }
      clearSharedMarks();
      if (signedIn && wantsSharing) {
        var uid = user.uid;
        sharedHl.enabled = true;
        sharedHl.uid = uid;
        sharedHl.pushDoc = function (idx, start, end) { pushDoc(db, uid, idx, start, end).then(function (ok) { if (ok && inSync) markSent(uid); }); };
        sharedHl.deleteDoc = function (idx, start, end) { deleteDoc(db, uid, idx, start, end).then(function (ok) { if (ok && inSync) markSent(uid); }); };
        // Backfill: push every highlight already saved locally, so turning
        // the toggle on (or signing in while it's already on) shares
        // everything made before this exact moment too, not just future
        // ones -- once per account per page load, and only when something
        // changed since the last complete send (see backfill() above).
        backfill(db, uid);
        subscribe(db, uid);
      } else {
        sharedHl.enabled = false;
        sharedHl.uid = null;
        sharedHl.pushDoc = function () {};
        sharedHl.deleteDoc = function () {};
      }
    }

    function boot() {
      var auth = firebase.auth();
      var db = firebase.firestore();
      auth.onAuthStateChanged(function (user) { applyState(db, user); });
      // turning sharing on is a deliberate act: it may backfill again (still skipped if nothing changed)
      window.addEventListener("shareHighlightsChanged", function () { backfilled = {}; applyState(db, auth.currentUser); });
    }

    if (window.__firebaseReady) boot();
    else window.addEventListener("firebaseReady", boot, { once: true });
  })();

  // Appended into the existing corner-action button group (id set by the
  // separate corner-buttons IIFE above, which has already run and built it
  // by the time this one executes) rather than duplicating makeCornerBtn's
  // setup here -- same visual button, just added from a different closure.
  var cornerGroup = document.getElementById("corner-actions");
  if (cornerGroup) {
    if (guideSearchHelp) {
      var searchBtn = document.createElement("button");
      searchBtn.type = "button";
      searchBtn.id = "guide-search-btn";
      searchBtn.className = "corner-btn";
      searchBtn.setAttribute("aria-label", "Search this guide");
      searchBtn.title = "Search this guide (/)";
      searchBtn.innerHTML = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>';
      searchBtn.addEventListener("click", guideSearchHelp.toggle);
      cornerGroup.appendChild(searchBtn);
    }

    var hlPanelBtn = document.createElement("button");
    hlPanelBtn.type = "button";
    hlPanelBtn.id = "hl-panel-btn";
    hlPanelBtn.className = "corner-btn";
    hlPanelBtn.setAttribute("aria-label", "Your highlights and notes");
    hlPanelBtn.title = "Your highlights and notes";
    hlPanelBtn.innerHTML = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>';
    hlPanelBtn.addEventListener("click", openHlPanel);
    cornerGroup.appendChild(hlPanelBtn);

    // "Add a note" (2026-10-15): click it, then click the spot (see setPlacing above). On a phone it
    // sits in the More menu like the other tools. Enter on it pins a note where you are reading.
    noteBtn = document.createElement("button");
    noteBtn.type = "button";
    noteBtn.id = "gnote-btn";
    noteBtn.className = "corner-btn";
    noteBtn.setAttribute("aria-label", "Add a note");
    noteBtn.setAttribute("aria-pressed", "false");
    noteBtn.title = "Add a note: click this, then click the spot in the guide";
    noteBtn.innerHTML = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15.5 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V8.5L15.5 3Z"/><path d="M15 3v6h6"/><path d="M12 11v6"/><path d="M9 14h6"/></svg>';
    noteBtn.addEventListener("click", function (e) {
      if (placing) { setPlacing(false); return; }
      if (e.detail === 0) { noteAtReadingSpot(); return; }    // keyboard
      setPlacing(true);
    });
    cornerGroup.appendChild(noteBtn);
  }
})();

/* ============================================================
   Guide hero disclosure on phones (design review item 12, 2026-09-25).
   The meta paragraphs after the first collapse behind a "Details" toggle
   at <=640px (CSS does the hiding; the toggle is inert on desktop, where
   the button is not displayed). Guides only: header.top + .guide-back-bar.
   ============================================================ */
(function () {
  if (!document.querySelector(".guide-back-bar")) return;
  var hero = document.querySelector("body > header.top");
  if (!hero) return;
  var metas = hero.querySelectorAll(":scope > p, :scope > .hdr-note, :scope > .hdr-save");
  var first = hero.querySelector(":scope > p");
  if (!first || metas.length < 2) return;
  hero.classList.add("hero-collapsible");
  var btn = document.createElement("button");
  btn.type = "button";
  btn.className = "hero-more";
  btn.setAttribute("aria-expanded", "false");
  btn.innerHTML = 'Details <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>';
  btn.addEventListener("click", function () {
    var open = hero.classList.toggle("hero-open");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
    btn.firstChild.nodeValue = open ? "Less " : "Details ";
  });
  // after the last collapsible meta, so it reads at the end of the visible line
  first.insertAdjacentElement("afterend", btn);
})();
