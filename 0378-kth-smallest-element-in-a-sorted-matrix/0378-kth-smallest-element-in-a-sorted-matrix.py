class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flat = sorted([num for row in matrix for num in row])
        return flat[k - 1]

        