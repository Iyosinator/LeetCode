class Solution:
    def separateDigits(self, nums):
        return [int(digit) for num in nums for digit in str(num)]
