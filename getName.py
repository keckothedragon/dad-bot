import constants

def getName(s: str, target: str):
    startIndex = s.lower().index(target) + len(target)
    endIndex = indexSoonest(s.lower(), startIndex)
    return s[startIndex : endIndex]

def indexSoonest(s: str, start: int):
    earliest = len(s)
    for x in constants.splits:
        try:
            i = s.index(x)
        except:
            continue
        if i < earliest and i > start:
            earliest = i
    return earliest