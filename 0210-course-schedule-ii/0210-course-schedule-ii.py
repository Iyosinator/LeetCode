class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]

        print(adj)

        in_degree = [0] * numCourses

        for ai, bi in prerequisites:
            adj[bi].append(ai)
            in_degree[ai] += 1

        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node)
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(ans) == numCourses:
            return ans
        else:
            return []