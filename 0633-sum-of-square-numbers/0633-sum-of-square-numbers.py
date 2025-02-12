class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))
        
        while left <= right:
            ans = (left ** 2) + (right**2)
            if ans == c:
                return True
            elif ans > c:
                right-=1
            else:
                left+=1
        return False

        

        