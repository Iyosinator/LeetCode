class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        num = 0

        for i in nums:
            num = (num * 2 + i) % 5
            ans.append(num == 0)
    
        return ans