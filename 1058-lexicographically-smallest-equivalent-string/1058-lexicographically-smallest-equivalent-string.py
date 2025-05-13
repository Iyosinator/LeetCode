class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {chr(i): chr(i) for i in range(ord('a'), ord('z') + 1)}
        
        def find(c):
            if parent[c] != c:
                parent[c] = find(parent[c])
            return parent[c]
        
        def union(c1, c2):
            root1, root2 = find(c1), find(c2)
            if root1 < root2:
                parent[root2] = root1
            else:
                parent[root1] = root2
        
        
        for a, b in zip(s1, s2):
            union(a, b)
        
     
        result = []
        for char in baseStr:
            result.append(find(char))
        
        return ''.join(result)
        