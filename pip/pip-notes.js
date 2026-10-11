/* Teach Pip: the student's own study notes, kept on this device. Loaded by
   pip/pip-window.js (and by the Settings row in pip/pip.js) only when it is needed.

   - Notes live in IndexedDB (database "pip-notes"), never in localStorage: cloud-sync
     uploads every localStorage key, and a student's notes must never leave the device.
   - Each note belongs to ONE exam (the exam's folder slug). Pip only ever searches the
     notes of the exam he is working on.
   - Text is read here in the browser: PDF with pdf.js, Word (.docx) with mammoth,
     .txt / .md as plain text. Both libraries come from cdnjs at exact versions and are
     checked against their SHA-384 hashes before they run, so a changed file on the CDN
     can never read a note. Pictures of text (photos, scanned PDFs) can't be read yet.
   - Nothing in this file sends anything anywhere. The window searches the blocks on the
     device; when Pip checks with Claude he sends at most two matching blocks, marked
     private so the server never shares them with anyone.

   Record (store "notes"): {id, exam, name, kind, added, bytes, pages, chars, blocks: [[page, text]]}
   A small "usage" store holds the same fields without the blocks, so listing notes and
   checking the limits never loads the text. */
(function () {
  "use strict";
  if (window.PipNotes) return;

  var DB = "pip-notes", NOTES = "notes", USAGE = "usage";
  // Limits (Teach Pip, 2026-10-08). Text is counted in characters.
  var LIMITS = { fileBytes: 15 * 1048576, perExam: 30, textTotal: 40 * 1048576 };
  var TARGET = 600, MAX = 800;                     // block size: about 600 characters, never over 800

  var CDN = "https://cdnjs.cloudflare.com/ajax/libs/";
  var PDF = { v: "5.4.624",
              main: CDN + "pdf.js/5.4.624/pdf.min.mjs", mainSri: "sha384-Sz0zpmM3DTX5AJnG6Qc9VZnPBjXzX4OjO9UOm6PItPVtUz/LCH89wd0yo16dMABB",
              worker: CDN + "pdf.js/5.4.624/pdf.worker.min.mjs", workerSri: "sha384-ZXs7afSvSrUNNZdgm8MicOVBn10qNAtAIL1289vJDfpdnuyL1xI+/hnNI9D3ukCU" };
  var MAMMOTH = { v: "1.12.3", url: CDN + "mammoth/1.12.3/mammoth.browser.min.js",
                  sri: "sha384-xqNXvcKbEqifokHcBnB0H32p+OQchhD/T/xJGWCMAW5fC0c0MBf9atO3weoPCT84" };

  function fail(code, extra) { var e = new Error(code); e.code = code; if (extra) for (var k in extra) e[k] = extra[k]; return e; }

  // ------------------------------------------------------------------ the database
  var dbP = null;
  // create=false only looks: when nothing was ever saved it resolves null and leaves no
  // empty database behind (opening Settings must not create one)
  function db(create) {
    if (dbP) return create ? dbP.then(function (d) { return d || db(true); }) : dbP;
    if (!window.indexedDB) return Promise.reject(fail("no_storage"));
    var p = new Promise(function (res, rej) {
      var rq, made = false;
      try { rq = indexedDB.open(DB, 1); } catch (e) { return rej(fail("no_storage")); }
      rq.onupgradeneeded = function (e) {
        if (!create && e.oldVersion === 0) { made = true; e.target.transaction.abort(); return; }
        var d = rq.result;
        if (!d.objectStoreNames.contains(NOTES)) d.createObjectStore(NOTES, { keyPath: "id" }).createIndex("exam", "exam");
        if (!d.objectStoreNames.contains(USAGE)) d.createObjectStore(USAGE, { keyPath: "id" }).createIndex("exam", "exam");
      };
      rq.onsuccess = function () {
        var d = rq.result;
        d.onversionchange = function () { d.close(); dbP = null; };    // "Delete all" in another tab
        res(d);
      };
      rq.onerror = function (e) {
        if (e && e.preventDefault) e.preventDefault();
        if (made) res(null); else rej(fail(rq.error && rq.error.name === "QuotaExceededError" ? "quota" : "no_storage"));
      };
      rq.onblocked = function () { rej(fail("busy")); };
    });
    dbP = p.then(function (d) { if (!d) dbP = null; return d; }, function (e) { dbP = null; throw e; });
    return dbP;
  }
  function req(r) {
    return new Promise(function (res, rej) { r.onsuccess = function () { res(r.result); }; r.onerror = function () { rej(r.error); }; });
  }
  function storeErr(e) {
    var n = e && (e.name || (e.inner && e.inner.name));
    return fail(n === "QuotaExceededError" ? "quota" : "write_failed");
  }

  // ------------------------------------------------------------------ change notices
  var stamp = 0, cache = {};
  var chan = null;
  try { chan = new BroadcastChannel("pip-notes"); chan.onmessage = function () { changed(true); }; } catch (e) {}
  function changed(remote) {
    stamp++; cache = {};
    if (!remote && chan) try { chan.postMessage(1); } catch (e) {}
    try { window.dispatchEvent(new CustomEvent("pip:notes")); } catch (e) {}
  }

  // ------------------------------------------------------------------ reading
  function list(exam) {                          // this exam's notes, oldest first, without their text
    return db(false).then(function (d) {
      if (!d) return [];
      return req(d.transaction(USAGE).objectStore(USAGE).index("exam").getAll(exam)).then(function (rows) {
        return rows.sort(function (a, b) { return a.added - b.added; });
      });
    });
  }
  function count() {                              // every note on this device
    return db(false).then(function (d) { return d ? req(d.transaction(USAGE).objectStore(USAGE).count()) : 0; })
      .catch(function () { return 0; });
  }
  function totals() {
    return db(false).then(function (d) {
      if (!d) return { files: 0, chars: 0 };
      return req(d.transaction(USAGE).objectStore(USAGE).getAll()).then(function (rows) {
        var c = 0; rows.forEach(function (r) { c += r.chars || 0; });
        return { files: rows.length, chars: c };
      });
    });
  }
  // the searchable blocks of one exam's notes: {stamp, items: [{id, name, page, text}]}
  function blocks(exam) {
    if (cache[exam]) return cache[exam];
    var at = stamp;
    var p = db(false).then(function (d) {
      if (!d) return [];
      return req(d.transaction(NOTES).objectStore(NOTES).index("exam").getAll(exam));
    }).then(function (recs) {
      var items = [];
      recs.sort(function (a, b) { return a.added - b.added; }).forEach(function (r) {
        r.blocks.forEach(function (b) { items.push({ id: r.id, name: r.name, page: b[0], text: b[1] }); });
      });
      return { stamp: at, items: items };
    });
    cache[exam] = p;
    p.catch(function () { if (cache[exam] === p) delete cache[exam]; });
    return p;
  }

  // ------------------------------------------------------------------ text out of a file
  function kindOf(file) {
    var n = String(file.name || "").toLowerCase(), t = String(file.type || "").toLowerCase();
    var ext = (n.match(/\.([a-z0-9]+)$/) || [])[1] || "";
    if (ext === "pdf" || t === "application/pdf") return "pdf";
    if (ext === "docx" || t === "application/vnd.openxmlformats-officedocument.wordprocessingml.document") return "docx";
    if (ext === "md" || ext === "markdown" || t === "text/markdown") return "md";
    if (ext === "txt" || t === "text/plain") return "txt";
    if (/^image\//.test(t) || /^(png|jpe?g|gif|webp|heic|heif|bmp|tiff?|svg)$/.test(ext)) return "picture";
    return null;
  }
  function verifiedURL(url, sri) {               // fetched with its hash checked, then run from this page's own origin
    return fetch(url, { integrity: sri, credentials: "omit", referrerPolicy: "no-referrer" }).then(function (r) {
      if (!r.ok) throw new Error("http " + r.status);
      return r.blob();
    }).then(function (b) { return URL.createObjectURL(new Blob([b], { type: "text/javascript" })); });
  }
  var pdfP = null, mamP = null;
  function pdfjs() {
    if (!pdfP) pdfP = Promise.all([verifiedURL(PDF.main, PDF.mainSri), verifiedURL(PDF.worker, PDF.workerSri)]).then(function (u) {
      return import(u[0]).then(function (lib) {
        if (!lib || !lib.getDocument || !lib.GlobalWorkerOptions) throw new Error("pdf.js missing");
        lib.GlobalWorkerOptions.workerSrc = u[1];   // the hash-checked worker (a module worker on this origin)
        return lib;
      });
    });
    pdfP.catch(function () { pdfP = null; });
    return pdfP;
  }
  function mammoth() {
    if (window.mammoth && window.mammoth.extractRawText) return Promise.resolve(window.mammoth);
    if (!mamP) mamP = new Promise(function (res, rej) {
      var s = document.createElement("script");
      s.src = MAMMOTH.url; s.integrity = MAMMOTH.sri; s.crossOrigin = "anonymous"; s.referrerPolicy = "no-referrer";
      s.onload = function () { if (window.mammoth && window.mammoth.extractRawText) res(window.mammoth); else rej(new Error("mammoth missing")); };
      s.onerror = function () { rej(new Error("mammoth load")); };
      document.head.appendChild(s);
    });
    mamP.catch(function () { mamP = null; });
    return mamP;
  }
  function pdfText(buf, onProgress) {
    return pdfjs().catch(function () { throw fail("reader_unavailable"); }).then(function (lib) {
      var task = lib.getDocument({ data: new Uint8Array(buf), isEvalSupported: false, disableFontFace: true,
                                   useSystemFonts: false, stopAtErrors: false, verbosity: 0 });
      return task.promise.catch(function (e) {
        throw fail(e && e.name === "PasswordException" ? "password" : "unreadable");
      }).then(function (doc) {
        var n = doc.numPages, out = [], i = 0;
        function next() {
          if (i >= n) { task.destroy(); return { pages: n, texts: out }; }
          i++;
          if (onProgress) onProgress(i, n);
          return doc.getPage(i).then(function (pg) { return pg.getTextContent(); }).then(function (tc) {
            var s = "";
            tc.items.forEach(function (it) { if (typeof it.str === "string") s += it.str + (it.hasEOL ? "\n" : ""); });
            out.push([i, s]);
            return next();
          }, function () { out.push([i, ""]); return next(); });
        }
        return next();
      });
    });
  }
  function docxText(buf) {
    return mammoth().catch(function () { throw fail("reader_unavailable"); }).then(function (m) {
      return m.extractRawText({ arrayBuffer: buf }).catch(function () { throw fail("unreadable"); });
    }).then(function (r) { return { pages: 0, texts: [[0, String(r && r.value || "")]] }; });
  }
  // .txt / .md are UTF-8 unless the file says (byte-order mark) or shows (every other byte is 0) that it
  // is UTF-16, which Windows Notepad ("Unicode") and PowerShell's ">" write. Read as UTF-8, UTF-16 comes
  // out as "M e t f o r m i n" that no search can ever match.
  function textEncoding(b) {
    if (b.length >= 2 && b[0] === 0xFF && b[1] === 0xFE) return "utf-16le";
    if (b.length >= 2 && b[0] === 0xFE && b[1] === 0xFF) return "utf-16be";
    if (b.length >= 3 && b[0] === 0xEF && b[1] === 0xBB && b[2] === 0xBF) return "utf-8";
    var n = Math.min(b.length, 65536), even = 0, odd = 0;
    for (var i = 0; i < n; i++) if (b[i] === 0) { if (i & 1) odd++; else even++; }
    if (even + odd > n * 0.3) return odd >= even ? "utf-16le" : "utf-16be";   // "M\0e\0" is little-endian
    return "utf-8";
  }
  function plainText(buf, md) {
    var s = new TextDecoder(textEncoding(new Uint8Array(buf))).decode(buf);   // the decoder drops the BOM
    // still full of U+FFFD (bytes that are not text) or NUL: a damaged file, a program renamed to .txt,
    // UTF-32... say it can't be read rather than keep garbage that search never finds
    var bad = 0, seen = 0;
    for (var i = 0; i < s.length; i++) {
      var c = s.charCodeAt(i);
      if (c === 0xFFFD || c === 0) { bad++; seen++; } else if (c > 32 && c !== 0xA0) seen++;
    }
    if (bad > seen * 0.1) throw fail("unreadable");
    if (md) s = s.replace(/^\s{0,3}#{1,6}\s+/gm, "").replace(/!\[[^\]]*\]\([^)]*\)/g, "")
      .replace(/\[([^\]]+)\]\([^)]*\)/g, "$1").replace(/(\*\*|__|`)/g, "");
    return { pages: 0, texts: [[0, s]] };
  }

  // ------------------------------------------------------------------ blocks of about 600 characters
  // on paragraph, then sentence, then word boundaries; a block never crosses a page
  // lone UTF-16 surrogates (half of an emoji or a math letter) become U+FFFD: the server refuses text
  // that is not well formed, which would make every Claude ask using that block fail
  function wellFormed(s) { return s.replace(/[\uD800-\uDBFF](?![\uDC00-\uDFFF])|(^|[^\uD800-\uDBFF])[\uDC00-\uDFFF]/g, function (m, pre) { return (pre || "") + "\uFFFD"; }); }
  function squash(s) { return wellFormed(s).replace(/[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/g, " ").replace(/\s+/g, " ").trim(); }
  function split(page, text, out) {
    var cur = "";
    function flush() { if (cur) out.push([page, cur]); cur = ""; }
    function addPiece(p) {
      if (!p) return;
      if (cur && cur.length + 1 + p.length > MAX) flush();
      cur = cur ? cur + " " + p : p;
      if (cur.length >= TARGET) flush();
    }
    String(text).replace(/\r\n?/g, "\n").split(/\n[ \t]*\n+/).forEach(function (para) {
      para = squash(para);
      if (!para) return;
      if (para.length <= MAX) { addPiece(para); return; }
      (para.match(/[^.!?]+(?:[.!?]+["')\]]*|$)\s*/g) || [para]).forEach(function (sen) {
        sen = sen.trim();
        while (sen.length > MAX) {                 // one very long sentence: cut it at a space
          var cut = sen.lastIndexOf(" ", TARGET); if (cut < TARGET / 2) cut = TARGET;
          var cc = sen.charCodeAt(cut); if (cc >= 0xDC00 && cc <= 0xDFFF) cut--;   // never split a surrogate pair
          addPiece(sen.slice(0, cut).trim()); flush(); sen = sen.slice(cut).trim();
        }
        addPiece(sen);
      });
    });
    flush();
  }
  function toBlocks(texts) { var out = []; texts.forEach(function (t) { split(t[0], t[1], out); }); return out; }

  // ------------------------------------------------------------------ adding and deleting
  var busy = Promise.resolve();                  // one file at a time, so the limits are checked in order
  function add(exam, file, onProgress) {
    var job = busy.then(function () { return addOne(exam, file, onProgress); });
    busy = job.catch(function () {});
    return job;
  }
  function addOne(exam, file, onProgress) {
    var kind = kindOf(file), name = String(file.name || "notes").slice(0, 160);
    if (kind === "picture") return Promise.reject(fail("picture", { file: name }));
    if (!kind) return Promise.reject(fail("unsupported", { file: name }));
    if (file.size > LIMITS.fileBytes) return Promise.reject(fail("too_big", { file: name }));
    if (!file.size) return Promise.reject(fail("no_text", { file: name }));
    return list(exam).then(function (rows) {
      if (rows.length >= LIMITS.perExam) throw fail("too_many", { file: name });
      for (var i = 0; i < rows.length; i++) if (rows[i].name === name && rows[i].bytes === file.size) throw fail("duplicate", { file: name });
      return file.arrayBuffer();
    }).then(function (buf) {
      if (onProgress) onProgress("reading");
      if (kind === "pdf") return pdfText(buf, function (i, n) { if (onProgress) onProgress("page", i, n); });
      if (kind === "docx") return docxText(buf);
      return plainText(buf, kind === "md");
    }).then(function (got) {
      var bl = toBlocks(got.texts), chars = 0, letters = 0;
      bl.forEach(function (b) { chars += b[1].length; letters += (b[1].match(/[A-Za-zÀ-ɏ]/g) || []).length; });
      // a scanned PDF or a document of pictures comes back with (almost) no letters
      if (letters < 20) throw fail(kind === "pdf" || kind === "docx" ? "picture" : "no_text", { file: name });
      return totals().then(function (t) {
        if (t.chars + chars > LIMITS.textTotal) throw fail("total_full", { file: name });
        var meta = { id: newId(), exam: exam, name: name, kind: kind, added: Date.now(), bytes: file.size,
                     pages: got.pages || 0, chars: chars, blocks: bl.length };
        var rec = { id: meta.id, exam: exam, name: name, kind: kind, added: meta.added, bytes: file.size,
                    pages: meta.pages, chars: chars, blocks: bl };
        return db(true).then(function (d) {
          return new Promise(function (res, rej) {
            var tx;
            try {
              tx = d.transaction([NOTES, USAGE], "readwrite");
              tx.objectStore(NOTES).put(rec);
              tx.objectStore(USAGE).put(meta);
            } catch (e) { try { tx && tx.abort(); } catch (e2) {} return rej(storeErr(e)); }
            tx.oncomplete = function () { res(meta); };
            tx.onabort = tx.onerror = function () { rej(storeErr(tx.error)); };
          });
        });
      });
    }).then(function (meta) {
      changed();
      try { if (navigator.storage && navigator.storage.persist) navigator.storage.persist(); } catch (e) {}
      return meta;
    }, function (e) {
      // our own failures carry a string code; anything else (a file the browser can't read) is "unreadable"
      if (e && typeof e.code === "string") { if (!e.file) e.file = name; throw e; }
      throw fail("unreadable", { file: name });
    });
  }
  function newId() {
    try { if (crypto.randomUUID) return crypto.randomUUID(); } catch (e) {}
    return Date.now().toString(36) + "-" + Math.random().toString(36).slice(2, 10);
  }
  function remove(id) {
    return db(false).then(function (d) {
      if (!d) return false;
      return new Promise(function (res, rej) {
        var tx = d.transaction([NOTES, USAGE], "readwrite");
        tx.objectStore(NOTES).delete(id); tx.objectStore(USAGE).delete(id);
        tx.oncomplete = function () { res(true); };
        tx.onabort = tx.onerror = function () { rej(storeErr(tx.error)); };
      });
    }).then(function (ok) { changed(); return ok; });
  }
  function removeAll() {                          // every note on this device, and the database itself
    var close = dbP ? dbP.then(function (d) { if (d) d.close(); }).catch(function () {}) : Promise.resolve();
    dbP = null;
    return close.then(function () {
      return new Promise(function (res) {
        if (!window.indexedDB) return res(false);
        var r = indexedDB.deleteDatabase(DB);
        r.onsuccess = function () { res(true); };
        r.onerror = function () { res(false); };
        r.onblocked = function () { /* other tabs close their copy on versionchange; success follows */ };
      });
    }).then(function (ok) { changed(); return ok; });
  }

  window.PipNotes = { add: add, list: list, blocks: blocks, remove: remove, removeAll: removeAll, count: count,
                      totals: totals, limits: LIMITS, kindOf: kindOf, versions: { pdfjs: PDF.v, mammoth: MAMMOTH.v },
                      _blocks: toBlocks };
})();
