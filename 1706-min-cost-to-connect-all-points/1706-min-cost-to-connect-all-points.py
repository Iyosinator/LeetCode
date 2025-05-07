class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        def distance(a,b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1]) 
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            parent[px] = py
            return True

        for i in range(n):
            for j in range(i+1,n):
                z = distance(points[i],points[j])
                edges.append((z,i,j))
                

        edges.sort()
        #return edges
        parent = list(range(n))

        cost = 0
        count = 0

        for z,i,j in edges:
            if union(i,j):
                cost += z
                count += 1
                if count == n-1:
                    break
        return cost



