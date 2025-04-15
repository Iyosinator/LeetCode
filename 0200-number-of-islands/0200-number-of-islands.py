class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def inbound(r,c):
            return 0 <= r < rows and 0 <= c < cols

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                row,col = q.popleft()

                for dx,dy in directions:
                    nx = row + dx
                    ny = col + dy
                    
                    if (inbound(nx,ny) and grid[nx][ny] == "1" and (nx,ny) not in visited):
                        q.append((nx,ny))
                        visited.add((nx,ny))                

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    bfs(r,c)    
        return islands