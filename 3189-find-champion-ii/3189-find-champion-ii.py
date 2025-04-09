class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        adj = [0] * n
        for x,y in edges:
            adj[y] -= 1
        res = -1
        s = float("-inf")
        #print(adj)
        for i in range(n):
            if adj[i] > s:
                res = i
                s = adj[i]
            elif adj[i] == s:
                res = -1
        return res