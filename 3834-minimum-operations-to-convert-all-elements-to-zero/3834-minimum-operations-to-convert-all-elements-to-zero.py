class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        stack = []
        
        for num in chain(nums, [0]):
            while stack and stack[-1] >= num:
                res += stack.pop() > num
            stack.append(num)
        return res
        '''
         nums = [0,2]
         n = 2



        '''