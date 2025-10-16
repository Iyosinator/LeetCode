from collections import Counter

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        count = Counter(x % value for x in nums)

        mex = 0
        while True:
            r = mex % value
            if count[r] > 0:
                count[r] -= 1 
                mex += 1     
            else:
                break           
        return mex
