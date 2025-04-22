class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        m = len(image)
        n = len(image[0])

        start = image[sr][sc]

        queue = deque([(sr, sc)])
        visited = set()

        if start == color:
            return image

        while queue:
            r, c = queue.popleft()

            if  r < 0 or r >= m or c < 0 or c >= n or image[r][c] != start:
                continue

            visited.add((r, c))
            image[r][c] = color



            queue.append((r + 1, c))
            queue.append((r - 1, c))
            queue.append((r, c + 1))
            queue.append((r, c - 1))

        return image
            

       
