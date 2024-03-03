def isSubsequence(self, s: str, t: str) -> bool:
    if s=="":
        return True

    s= list(s)
    t= list(t)
    for x in t:

        if x == s[0]:
            s.pop(0)
        if len(s)==0:
            return True

    if len(s)>0:
        return False


