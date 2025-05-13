class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)],
        }
        
        queue = deque([(0, 0)])
        visited = set([(0, 0)])
        
        while queue:
            i, j = queue.popleft()
            
            if (i, j) == (m - 1, n - 1):
                return True
            
            for di, dj in directions[grid[i][j]]:
                ni, nj = i + di, j + dj
                
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    if (-di, -dj) in directions[grid[ni][nj]]:
                        queue.append((ni, nj))
                        visited.add((ni, nj))
        
        return False