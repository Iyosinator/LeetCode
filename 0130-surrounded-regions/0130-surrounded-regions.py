class Solution:
    def solve(self, board: List[List[str]]) -> None:

        m = len(board)
        n = len(board[0])
        queue = deque()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def inbound(x,y):
            return 0<= x < m and 0<= y < n

        def border(i,j):
            return (i == 0 or i == m - 1 or j == 0 or j == n - 1) and board[i][j] == "O"


        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        for i in range(m):
            for j in range(n):
                if border(i,j):
                    queue.append((i,j))
                    board[i][j] = "S"

        while queue:
            x, y = queue.popleft()
            for dx,dy in directions:
                nx, ny = x + dx, y + dy

                if inbound(nx,ny) and board[nx][ny] == 'O':
                    queue.append((nx,ny))
                    board[nx][ny] = "S"
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'


        