class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counter = set(nums)
        for num in counter:
            if num in nums:
                nums.remove(num)
        return nums

