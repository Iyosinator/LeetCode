class Solution:
    def smallestNumber(self, n: int) -> int:
        def helper(k, prev):
            if prev >= n:
                return prev
            return helper(k + 1, prev + 2 ** k)
        
        return helper(1, 1)
