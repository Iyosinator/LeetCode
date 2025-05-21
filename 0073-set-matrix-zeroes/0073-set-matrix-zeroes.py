class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])


        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    for k in range(cols):
                        if matrix[i][k] != 0:
                            matrix[i][k] = 'X'
                    for k in range(rows):
                        if matrix[k][j] != 0:
                            matrix[k][j] = 'X'

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 'X':
                    matrix[i][j] = 0
              
        
