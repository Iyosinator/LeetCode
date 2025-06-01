class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        count = 0
        for x in range(min(n, limit) + 1):
            rest = n - x
            if rest > 2 * limit:
                continue
            y_min = max(0, rest - limit)
            y_max = min(limit, rest)
            count += y_max - y_min + 1
        return count

