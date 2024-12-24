class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dictS = {}
        dictT= {}

        for i in range(len(s)):
            dictS[s[i]] = dictS.get(s[i],0) + 1
            dictT[t[i]] = dictT.get(t[i],0) + 1
        for c in dictS:
            if dictS[c] != dictT.get(c,0):
                return False
        return True        