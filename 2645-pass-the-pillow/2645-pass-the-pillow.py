class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle = time % (2 * (n - 1))
        return 1 + cycle if cycle < n - 1 else 2 * n - 1 - cycle
