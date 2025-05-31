class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        #print(rows,cols)
        def inbound(i,j):
            return 0 <= i < rows and 0 <= j < cols

        for i in range(rows):
            for j in range(cols):
               
                if rows == 1:
                    return True
                elif inbound(i,j) and inbound(i+1,j+1)  and matrix[i][j] != matrix[i+1][j+1]:
                
                    return False
                
        return True

        