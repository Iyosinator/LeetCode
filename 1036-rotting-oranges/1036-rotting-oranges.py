from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        fresh_count = 0
        minutes = 0

        def inbound(x, y):
            return 0 <= x < m and 0 <= y < n 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        while queue:
            for i in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if inbound(nx, ny) and grid[nx][ny] == 1 and (nx, ny) not in visited:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        visited.add((nx, ny)) 
                        fresh_count -= 1
            minutes += 1

        return -1 if fresh_count > 0 else minutes - 1
