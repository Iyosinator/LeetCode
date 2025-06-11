class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        current_max = nums[0]
        for i in range(1, len(nums)):
            current_max = max(nums[i], current_max + nums[i])
            max_so_far = max(max_so_far, current_max)
            
        min_so_far = nums[0]
        current_min = nums[0]
        for i in range(1, len(nums)):
            current_min = min(nums[i], current_min + nums[i])
            min_so_far = min(min_so_far, current_min)
            
        return max(abs(max_so_far), abs(min_so_far))
