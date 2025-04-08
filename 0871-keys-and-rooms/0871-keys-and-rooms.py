class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0,}
        def dfs(k):
            for room in rooms[k]:
                if room not in visited:
                    visited.add(room)
                    dfs(room)
        dfs(0)
        if len(visited) == len(rooms): return True
        return False