class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            m = (left + right) // 2
            if (m*m) == x:
                return m
            elif (m**2) > x:
                right = m-1
            else:
                left = m + 1
        return right
        