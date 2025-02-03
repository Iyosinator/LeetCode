class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            if complement in store:
                return [store[complement],i]
            store[nums[i]] = i
        return []
        