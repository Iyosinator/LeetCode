class Solution:
    def triangleType(self, nums: List[int]) -> str:
        x = Counter(nums)
        i,j,k = 0,1,2
        if  (nums[i] + nums[j] <= nums[k]) or (nums[j] + nums[k] <= nums[i]) or (nums[k] + nums[i] <= nums[j]):
            return "none"
        elif len(x) == 1:
            return "equilateral"
        elif len(x) == 2:
            return "isosceles"
        elif len(x) == 3:
            return "scalene"
        

        