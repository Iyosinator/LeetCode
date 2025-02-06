class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = collections.Counter()
        ans = 0
        for i in range(len(nums)):
            for j in range(i):
                res = nums[i] * nums[j]
                ans+=count[res] * 8
                count[res] += 1
        return ans
                   

        

        