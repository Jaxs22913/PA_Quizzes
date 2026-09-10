def append(path, block):
    s=open(path,encoding="utf-8").read().rstrip()
    assert s.endswith("]"), "expected the list to close the file"
    open(path,"w",encoding="utf-8").write(s[:-1].rstrip()+"\n"+block+"\n]\n")
