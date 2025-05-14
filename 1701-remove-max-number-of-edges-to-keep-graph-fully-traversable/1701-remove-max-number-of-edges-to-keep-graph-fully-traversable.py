class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.components = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.size[xr] < self.size[yr]:
            xr, yr = yr, xr
        self.parent[yr] = xr
        self.size[xr] += self.size[yr]
        self.components -= 1
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        a = DSU(n)
        b = DSU(n)
        used = 0
        for t, u, v in edges:
            if t == 3:
                ua = a.union(u, v)
                ub = b.union(u, v)
                if ua or ub:
                    used += 1
        for t, u, v in edges:
            if t == 1 and a.union(u, v):
                used += 1
            if t == 2 and b.union(u, v):
                used += 1
        if a.components > 1 or b.components > 1:
            return -1
        return len(edges) - used
        
        