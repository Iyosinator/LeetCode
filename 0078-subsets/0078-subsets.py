class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        total = 1 << n  
        res = []

        for mask in range(total):
            subset = []
            for i in range(n):
                if (mask >> i) & 1:
                    subset.append(nums[i])
            res.append(subset)

        return res
