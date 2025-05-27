class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        x  = set(jewels)
        count  = 0
        for stone in stones:
            if stone in x:
                count += 1
        return count