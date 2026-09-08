import sys
def append(block):
    p="_cmse3_leadins.py"; s=open(p,encoding="utf-8").read().rstrip()
    assert s.endswith("}"), "expected the dict to be the last thing in the file"
    open(p,"w",encoding="utf-8").write(s[:-1].rstrip()+"\n"+block+"\n}\n")
