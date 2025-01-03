class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        nums=list(accumulate(nums))
        return sum(1 if 2*x>=nums[-1] else 0 for x in nums[0:len(nums)-1])