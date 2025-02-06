class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                ans.append(nums[i])
                if len(nums) <= 1:
                    return []        
        return ans


        