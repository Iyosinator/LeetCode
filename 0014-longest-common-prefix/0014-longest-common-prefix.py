class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        x, y = min(strs), max(strs)
    
        z = 0
        while z < len(x) and x[z] == y[z]:
            z += 1

        return x[:z]
