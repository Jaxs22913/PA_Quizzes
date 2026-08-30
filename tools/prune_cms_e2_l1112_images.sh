#!/bin/sh
# Downscale the Lecture 11/12 images that the chart and guide actually use to
# 600 px JPEG quality 80, and delete every other extracted original.
#
# extract_cms_e2_l1112_images.py writes all 50 images at full size, which takes
# this folder from 2.5 MB to 47 MB. Run this straight after it.
set -e
D="$(dirname "$0")/../Clinical Medicine and Surgery I Exam 2/cms-ophtho-chart-images"
KEEP="l11-s004_1 l11-s020_1 l11-s039_2 l11-s052_1 l12-s012_1 l12-s019_1 \
l12-s023_3 l12-s028_1 l12-s045_1 l12-s045_2 l12-s045_3 l12-s045_4"
cd "$D"
for b in $KEEP; do
  src=$(ls "$b".* 2>/dev/null | grep -v '\.jpg$' | head -1) || true
  [ -n "$src" ] && sips -s format jpeg -s formatOptions 80 -Z 600 "$src" --out "$b.jpg" >/dev/null
done
for f in l11-* l12-*; do
  case " $(echo $KEEP | sed 's/[^ ]*/&.jpg/g') " in *" $f "*) ;; *) rm -f "$f";; esac
done
echo "kept $(ls l11-* l12-* | wc -l | tr -d ' ') images; folder now $(du -sh . | cut -f1)"
