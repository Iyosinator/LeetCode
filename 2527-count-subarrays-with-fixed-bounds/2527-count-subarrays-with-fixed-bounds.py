class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        left_bound = -1
        min_pos = -1
        max_pos = -1
        
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                left_bound = i
            if num == minK:
                min_pos = i
            if num == maxK:
                max_pos = i
            
            if min_pos != -1 and max_pos != -1:
                count += max(0, min(min_pos, max_pos) - left_bound)
        
        return count
        