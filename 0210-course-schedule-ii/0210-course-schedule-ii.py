class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        # 1 White 2 Gray 3 Black
        
        for a, b in prerequisites:
            graph[b].append(a)
       
        visited = [0] * numCourses
        order = []

        def dfs(course):
            if visited[course] == 1:  
                return False
            if visited[course] == 2:  
                return True
            
            visited[course] = 1  
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
        
            visited[course] = 2  
            order.append(course)  
            return True
        for course in range(numCourses):
            if visited[course] == 0:  
                if not dfs(course):
                    return []
        
        return order[::-1] 
