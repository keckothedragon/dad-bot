def getName(s: str, target: str):
    if " im " in s:
        s = s.split(" " + target + " ", 1)
        while not s[1]:
            s.pop(1)
        s = s[1]
    else:
        s = s.split(target)[1]
    s = s.strip(' ')
    return splitSoonest(s)

def splitSoonest(s: str):
    splits = ['\"','.',')','(','?','!','\'']
    for c in s:
        if c in splits:
            return s.split(c)[0]
    return s