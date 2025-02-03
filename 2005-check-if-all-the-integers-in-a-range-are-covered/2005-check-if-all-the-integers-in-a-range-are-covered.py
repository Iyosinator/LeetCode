class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = set()
        for start, end in ranges:
            covered.update(range(start, end + 1)) 
        return all(i in covered for i in range(left, right + 1))

        