class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        result = []
        diagonals = {}

        if not mat:
            return []
        
        for i in range(m):
            for j in range(n):
                if i + j not in diagonals:
                    diagonals[i + j] = []
                
                diagonals[i + j].append(mat[i][j])

        
        for k in range(m + n - 1):
            if k % 2 == 0:
                result.extend(diagonals[k][::-1])
            else:
                result.extend(diagonals[k])

        return result


        