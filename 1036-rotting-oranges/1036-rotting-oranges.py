from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        minutes = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        def inbound(x, y):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    yield nx, ny

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for nx, ny in inbound(x, y):
                    grid[nx][ny] = 2
                    queue.append((nx, ny))
                    fresh_count -= 1
            minutes += 1

        return -1 if fresh_count > 0 else minutes - 1
