class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        for i in range(rows-1):
            for j in range(columns-1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True


