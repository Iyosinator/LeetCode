class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums.sort(key = lambda x:x*10,reverse= True)
        result = ''.join(nums)
        if result[0] != "0":
            return result
        else:
            return '0'



        