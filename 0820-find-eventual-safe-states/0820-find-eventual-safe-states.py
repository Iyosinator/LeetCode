class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = [0] * n
        
        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            state[node] = 1 
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            state[node] = 2 
            return True
        
        safe_nodes = []
        for i in range(n):
            if dfs(i):
                safe_nodes.append(i)
        
        return safe_nodes

         