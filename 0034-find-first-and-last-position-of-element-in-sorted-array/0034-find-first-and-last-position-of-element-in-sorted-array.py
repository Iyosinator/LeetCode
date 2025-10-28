class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def lower_bound(nums,target):
            left = 0
            right = len(nums)
            while left < right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        def upper_bound(nums,target):
            left = 0
            right = len(nums)
            while left < right:
                mid  = (left + right) // 2

                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left

        lower_bound = lower_bound(nums,target)
        upper_bound = upper_bound(nums,target) - 1

        if lower_bound < len(nums) and nums[lower_bound] == target:
            return [lower_bound,upper_bound]
        else:
            return [-1,-1]
        