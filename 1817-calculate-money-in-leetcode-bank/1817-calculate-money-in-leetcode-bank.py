class Solution:
    def totalMoney(self, n: int) -> int:
        full_week = n//7
        left_days = (n-7*(n//7))

        x = (7* (full_week) * (full_week + 7)) / 2
        y = (left_days * full_week) + (left_days *(left_days + 1)) /2
        if n <= 7:
            return int(n *(n+1) /2)
        else:
            return int(x+y)            

