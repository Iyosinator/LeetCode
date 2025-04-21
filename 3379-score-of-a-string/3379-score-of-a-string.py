class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(1,n):
            diff = abs(ord(s[i-1]) - ord(s[i]))
            ans += diff
        return ans
            