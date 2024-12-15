class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:  # Case 1: Red (0)
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:  # Case 2: White (1)
                mid += 1
            else:  # Case 3: Blue (2)
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
