class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = 0

        while len(nums) != len(set(nums)):
            nums = nums[3:]
            counter += 1
        return counter
        