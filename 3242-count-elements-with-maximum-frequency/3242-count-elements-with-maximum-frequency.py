class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        x = Counter(nums)
        
        y = sorted(x.values())
        count = 0

        m = y[-1]

        for i in range(len(y)):
            if y[i] == m:
                count += y[i]

        return count