#!/bin/sh
# Downscale the Lecture 11/12 images that the chart and guide actually use to
# 600 px JPEG quality 80, and delete every other extracted original.
#
# extract_cms_e2_l1112_images.py writes all 50 images at full size, which takes
# this folder from 2.5 MB to 47 MB. Run this straight after it.
set -e
# The l13-* entries are each the picture that slide's own A/B/C/D or
# ABOVE/BELOW label points at, resolved by geometry rather than by extraction
# order -- see tools/_cms_e2_l13_figures.py. Picking by number would have put
# soft drusen under the disciform-scar caption.
D="$(dirname "$0")/../Clinical Medicine and Surgery I Exam 2/cms-ophtho-chart-images"
# l12-s023 slide 23 labels its pictures ABOVE / MIDDLE / BELOW. _1 is the ABOVE
# one -- the fundus photograph of optic nerve swelling -- and _3 is BELOW, the
# periventricular FLAIR. Keeping only _3 left the guide showing a brain MRI
# under a caption about the optic disc, so both are kept now.
KEEP="l11-s004_1 l11-s020_1 l11-s039_2 l11-s052_1 l12-s012_1 l12-s019_1 \
l12-s023_1 l12-s023_3 l12-s028_1 l12-s045_1 l12-s045_2 l12-s045_3 l12-s045_4 \
l13-s011_1 l13-s011_3 l13-s032_1 l13-s037_1 l13-s037_2 l13-s038_2 \
l13-s041_1 l13-s044_4 l13-s048_1 l13-s052_1"
cd "$D"
for b in $KEEP; do
  src=$(ls "$b".* 2>/dev/null | grep -v '\.jpg$' | head -1) || true
  [ -n "$src" ] && sips -s format jpeg -s formatOptions 80 -Z 600 "$src" --out "$b.jpg" >/dev/null
done
for f in l11-* l12-* l13-*; do
  case " $(echo $KEEP | sed 's/[^ ]*/&.jpg/g') " in *" $f "*) ;; *) rm -f "$f";; esac
done
echo "kept $(ls l11-* l12-* l13-* | wc -l | tr -d ' ') images; folder now $(du -sh . | cut -f1)"
