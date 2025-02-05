class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 != n2:
            return False
    
        mismatch = 0

        for i in range(min(n1,n2)):
            if s1[i] != s2[i]:
                mismatch +=1
        #return mismatch
        
        if (sorted(s1) == sorted(s2)) and (mismatch <= 2):
            return True
        else:
            return False

