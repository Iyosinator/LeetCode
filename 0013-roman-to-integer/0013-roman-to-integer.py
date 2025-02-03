class Solution:
    def romanToInt(self, s: str) -> int:
        romanToIntDict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        ans = 0
        for i in range(len(s)):
            value = romanToIntDict[s[i]]
            if i < len(s) -1 and value < romanToIntDict[s[i+1]]:
                ans-=value
            else:
                ans+=value
        return ans

        