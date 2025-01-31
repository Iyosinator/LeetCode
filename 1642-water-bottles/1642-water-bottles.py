class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        num = res
        while num >= numExchange:
            rem = num % numExchange
            free = num // numExchange
            num = rem + free
            res+=free
        return res
        