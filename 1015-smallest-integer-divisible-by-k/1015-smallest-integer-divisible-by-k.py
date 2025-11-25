class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        '''
        1:- 1
        11:- 1,2
        111
        1111
        '''
        if k%2 == 0 or k%5 == 0:
            return -1
        else:
            cur = 1
            res = 1
            
            while cur%k!=0:
                cur = (10*cur+1)%k
                res += 1
            return res
            