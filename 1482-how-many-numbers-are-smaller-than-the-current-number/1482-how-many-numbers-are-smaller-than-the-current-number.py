class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums)
        result = []
        counter = {}

        for i in range(len(nums)):
            if sortedNums[i] not in counter:
                counter[sortedNums[i]] = i
        result = []
        for num in nums:
            result.append(counter[num])
        
        return result
        
        