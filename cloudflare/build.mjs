#!/usr/bin/env node
// Build the Cloudflare copy of PA Quizzes into ./dist. See docs/HOSTING_CLOUDFLARE.md.
//
// The repo root IS the site (GitHub Pages publishes it as-is under /PA_Quizzes/).
// For Cloudflare the same files go to dist/PA_Quizzes/, so every page address,
// and every saved-progress key derived from location.pathname, is identical on
// both hosts. Nothing is transformed: files are copied byte for byte.
//
// Only git-tracked files are published (no .DS_Store, no ignored scratch), minus
// build tooling that no page links to. cloudflare/_redirects, _headers and
// 404.html go to the dist root, where Workers Static Assets reads them;
// cloudflare/import.html (the cutover hand-off receiver) goes to /PA_Quizzes/.
//
// One generated folder is copied although git ignores it: pip/data/ (Pip's question
// banks and guide index), written by tools/build_pip_data.py, which the deploy workflow
// runs just before this script. A tree that ships pip/pip.js without that data stops
// the build, so Pip is never deployed with nothing to search.
//
//   node cloudflare/build.mjs        (.github/workflows/cloudflare.yml runs this on every push)

import { execFileSync } from 'node:child_process'
import { copyFileSync, constants, existsSync, mkdirSync, readdirSync, rmSync, statSync } from 'node:fs'
import { dirname, join, relative, sep } from 'node:path'
import { fileURLToPath } from 'node:url'

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..')
const DIST = join(ROOT, 'dist')
const SITE = join(DIST, 'PA_Quizzes')

// Top-level paths that are tooling or hosting config, never linked by a page
// (verified 2026-10-08: 0 of 1,343 pages reference tools/).
const EXCLUDE_TOP = new Set([
  '.github', 'tools', 'cloudflare', 'docs', 'dist', 'node_modules', '.wrangler',
  'wrangler.jsonc', 'package.json', 'package-lock.json',
  'CLAUDE.md', 'firestore.rules', '.gitignore', '.nojekyll',
  'superbrain',   // the helper Worker's source; deployed on its own, never served as site files
])
const FILE_LIMIT = 20000          // Workers Free: files per version
const SIZE_LIMIT = 25 * 1024 * 1024  // per file

function trackedFiles() {
  try {
    const out = execFileSync('git', ['ls-files', '-z'], { cwd: ROOT, maxBuffer: 64 << 20 })
    return out.toString('utf8').split('\0').filter(Boolean)
  } catch {
    // No git (unusual for Workers Builds, which clones the repo): walk the tree.
    const files = []
    const walk = d => {
      for (const name of readdirSync(join(ROOT, d))) {
        if (name === '.git' || name === '.DS_Store') continue
        const rel = d ? `${d}/${name}` : name
        statSync(join(ROOT, rel)).isDirectory() ? walk(rel) : files.push(rel)
      }
    }
    walk('')
    return files
  }
}

rmSync(DIST, { recursive: true, force: true })
mkdirSync(SITE, { recursive: true })

let count = 0, bytes = 0
const tooBig = []
const published = new Set()
function publish(rel) {
  if (published.has(rel)) return            // the no-git fallback already walked it
  const src = join(ROOT, rel)
  if (!existsSync(src)) return              // deleted in the working tree
  const size = statSync(src).size
  if (size > SIZE_LIMIT) { tooBig.push(rel); return }
  const dst = join(SITE, rel)
  mkdirSync(dirname(dst), { recursive: true })
  copyFileSync(src, dst, constants.COPYFILE_FICLONE)   // instant clone on APFS, plain copy elsewhere
  published.add(rel)
  count++; bytes += size
}
const tracked = trackedFiles()
for (const rel of tracked) {
  if (EXCLUDE_TOP.has(rel.split('/')[0])) continue
  if (rel.startsWith('pip/explain/')) continue   // Pip's explanation sources; pip/data/explain/ is what ships
  publish(rel)
}

// Pip's generated data (git-ignored; see the header).
if (tracked.includes('pip/pip.js')) {
  const DATA = 'pip/data'
  if (!existsSync(join(ROOT, DATA, 'index.json'))) {
    console.error(`ERROR: pip/pip.js is published but ${DATA}/index.json is missing. Run python3 tools/build_pip_data.py first.`)
    process.exit(1)
  }
  let pipFiles = 0
  const walk = d => {
    for (const name of readdirSync(join(ROOT, d)).sort()) {
      if (name === '.DS_Store') continue
      const rel = `${d}/${name}`
      if (statSync(join(ROOT, rel)).isDirectory()) walk(rel)
      else { publish(rel); if (published.has(rel)) pipFiles++ }
    }
  }
  walk(DATA)
  console.log(`${DATA}/: ${pipFiles} generated files`)
}

for (const name of ['_redirects', '_headers', '404.html']) {
  copyFileSync(join(ROOT, 'cloudflare', name), join(DIST, name))
  count++
}
// Cutover hand-off receiver (inert until the GitHub Pages "moved" page opens it).
if (existsSync(join(SITE, 'import.html'))) throw new Error('site already has an import.html; rename cloudflare/import.html')
copyFileSync(join(ROOT, 'cloudflare', 'import.html'), join(SITE, 'import.html'))
count++

if (tooBig.length) {
  console.error(`ERROR: ${tooBig.length} file(s) over 25 MiB cannot be deployed:\n  ${tooBig.join('\n  ')}`)
  process.exit(1)
}
if (count > FILE_LIMIT) {
  console.error(`ERROR: ${count} files exceeds the ${FILE_LIMIT}-file limit for one Worker version.`)
  process.exit(1)
}
console.log(`dist/: ${count} files, ${(bytes / 1048576).toFixed(1)} MiB (site under /PA_Quizzes/, ${relative(ROOT, DIST)}${sep})`)
