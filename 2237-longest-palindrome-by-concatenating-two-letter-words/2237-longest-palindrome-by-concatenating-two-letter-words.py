class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        c = Counter(words)
        res = center = 0
        for w in c:
            rev = w[::-1]
            if w == rev:
                res += (c[w] // 2) * 4
                if c[w] % 2: center = 2
            else:
                res += min(c[w], c[rev]) * 2
        return res + center
