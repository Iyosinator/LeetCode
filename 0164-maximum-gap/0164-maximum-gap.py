class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maximum = 0
        for i in range(1,len(nums)):
            diff = nums[i] - nums[i-1]
            maximum = max(diff,maximum)
        return maximum
        