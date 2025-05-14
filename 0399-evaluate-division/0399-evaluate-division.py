class Solution:
    class DSU:
        def __init__(self):
            self.parent = {}
            self.weight = {}

        def find(self, node):
            if node != self.parent[node]:
                original_parent = self.parent[node]
                self.parent[node] = self.find(original_parent)
                self.weight[node] *= self.weight[original_parent]
            return self.parent[node]

        def union(self, node1, node2, value):
            if node1 not in self.parent:
                self.parent[node1] = node1
                self.weight[node1] = 1.0
            if node2 not in self.parent:
                self.parent[node2] = node2
                self.weight[node2] = 1.0
            root1, root2 = self.find(node1), self.find(node2)
            if root1 != root2:
                self.parent[root1] = root2
                self.weight[root1] = value * self.weight[node2] / self.weight[node1]

        def isConnected(self, node1, node2):
            return node1 in self.parent and node2 in self.parent and self.find(node1) == self.find(node2)

        def getRatio(self, node1, node2):
            return self.weight[node1] / self.weight[node2]

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dsu = self.DSU()
        for (var1, var2), val in zip(equations, values):
            dsu.union(var1, var2, val)
        return [dsu.getRatio(var1, var2) if dsu.isConnected(var1, var2) else -1.0 for var1, var2 in queries]
