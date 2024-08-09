class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_indices = [(value, index) for index, value in enumerate(nums)]
        nums_with_indices.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            current_sum = nums_with_indices[left][0] + nums_with_indices[right][0]
            if current_sum == target:
                return [nums_with_indices[left][1], nums_with_indices[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return [] 

