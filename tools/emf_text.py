#!/usr/bin/env python3
"""Read the TEXT out of the enhanced-metafile (.emf) pictures inside a .pptx.

A slide that looks like a table but extracts as empty is often an embedded Word/Excel table stored as an
.emf picture. OCR cannot read EMF (Pillow and macOS Vision both fail, qlmanage hangs), but an EMF is a list
of drawing records, and the words are drawn by EMR_EXTTEXTOUTW records, so the text (and its position) can
be read straight out of the file. Arrows come through as Symbol-font private-use characters:
U+F0AD is an up arrow, U+F0AF a down arrow, U+F0AE right, U+F0AC left.

    python3 tools/emf_text.py path/to/image.emf ...        # rows reconstructed by vertical position
    unzip -o deck.pptx 'ppt/media/*' 'ppt/slides/_rels/*'  # then find which slide uses which image in the .rels

Found 2026-09-29 to recover the ENT deck's histamine-receptor and antihistamine tables and the
antihypertensive deck's beta-blocker and vasodilator tables (see pharm_e2_reference_charts memory).
"""
import struct,sys
def emf_text(path):
    d=open(path,'rb').read(); out=[]; o=0
    while o+8<=len(d):
        t,sz=struct.unpack_from('<II',d,o)
        if sz<8: break
        if t==84:   # EMR_EXTTEXTOUTW
            x,y,n,off=struct.unpack_from('<iiII',d,o+36)
            s=d[o+off:o+off+2*n].decode('utf-16le','ignore')
            out.append((y,x,s))
        elif t==83:
            x,y,n,off=struct.unpack_from('<iiII',d,o+36)
            out.append((y,x,d[o+off:o+off+n].decode('latin1','ignore')))
        o+=sz
    return out
def rows(items,tol=6):
    items=sorted(items); res=[]; cur=[]
    for y,x,s in items:
        if cur and abs(y-cur[0][0])>tol:
            res.append(cur); cur=[]
        cur.append((y,x,s))
    if cur: res.append(cur)
    return [" | ".join(s for _,_,s in sorted(r,key=lambda t:t[1])) for r in res]
if __name__=='__main__':
    for p in sys.argv[1:]:
        it=emf_text(p); print('#####',p,len(it),'text records')
        for r in rows(it): print(r)
