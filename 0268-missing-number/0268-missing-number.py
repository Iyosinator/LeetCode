class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_array = []
        unique_number = []
        for i in range(0,n+1):
            expected_array.append(i)
        for y in expected_array:
            if y not in nums:
                return y