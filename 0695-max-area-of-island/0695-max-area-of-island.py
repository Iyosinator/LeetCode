class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  


        def inbound(r,c):
            return 0 <= r < rows and 0 <= c < cols

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    queue = deque()
                    queue.append((r, c))
                    grid[r][c] = 0  
                    area = 1

                    while queue:
                        cr, cc = queue.popleft()
                        
                        for dr, dc in directions:
                          
                            nr = cr + dr
                            nc = cc + dc

                            if inbound(nr,nc) and grid[nr][nc] == 1:
                                grid[nr][nc] = 0 
                                queue.append((nr, nc))
                                area += 1

                    max_area = max(max_area, area)

        return max_area