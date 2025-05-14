class Solution:
    class DSU:
        def __init__(self):
            self.parent = {}
            self.weight = {}

        def find(self, x):
            if x != self.parent[x]:
                orig_parent = self.parent[x]
                self.parent[x] = self.find(orig_parent)
                self.weight[x] *= self.weight[orig_parent]
            return self.parent[x]

        def union(self, x, y, value):
            if x not in self.parent:
                self.parent[x] = x
                self.weight[x] = 1.0
            if y not in self.parent:
                self.parent[y] = y
                self.weight[y] = 1.0
            px, py = self.find(x), self.find(y)
            if px != py:
                self.parent[px] = py
                self.weight[px] = value * self.weight[y] / self.weight[x]

        def isConnected(self, x, y):
            return x in self.parent and y in self.parent and self.find(x) == self.find(y)

        def getRatio(self, x, y):
            return self.weight[x] / self.weight[y]

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dsu = self.DSU()
        for (a, b), val in zip(equations, values):
            dsu.union(a, b, val)
        return [dsu.getRatio(a, b) if dsu.isConnected(a, b) else -1.0 for a, b in queries]
