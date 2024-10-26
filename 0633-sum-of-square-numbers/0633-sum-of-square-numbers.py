class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))

        while left <= right:
            total = (right**2) + (left**2)
            if total == c:
                return True
            elif total > c:
                right-=1
            else:
                left+=1
        return False
        