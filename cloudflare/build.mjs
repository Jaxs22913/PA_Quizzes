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
// 404.html go to the dist root, where Workers Static Assets reads them.
//
//   node cloudflare/build.mjs        (Workers Builds runs this as the build command)

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
for (const rel of trackedFiles()) {
  if (EXCLUDE_TOP.has(rel.split('/')[0])) continue
  const src = join(ROOT, rel)
  if (!existsSync(src)) continue            // deleted in the working tree
  const size = statSync(src).size
  if (size > SIZE_LIMIT) { tooBig.push(rel); continue }
  const dst = join(SITE, rel)
  mkdirSync(dirname(dst), { recursive: true })
  copyFileSync(src, dst, constants.COPYFILE_FICLONE)   // instant clone on APFS, plain copy elsewhere
  count++; bytes += size
}

for (const name of ['_redirects', '_headers', '404.html']) {
  copyFileSync(join(ROOT, 'cloudflare', name), join(DIST, name))
  count++
}

if (tooBig.length) {
  console.error(`ERROR: ${tooBig.length} file(s) over 25 MiB cannot be deployed:\n  ${tooBig.join('\n  ')}`)
  process.exit(1)
}
if (count > FILE_LIMIT) {
  console.error(`ERROR: ${count} files exceeds the ${FILE_LIMIT}-file limit for one Worker version.`)
  process.exit(1)
}
console.log(`dist/: ${count} files, ${(bytes / 1048576).toFixed(1)} MiB (site under /PA_Quizzes/, ${relative(ROOT, DIST)}${sep})`)
