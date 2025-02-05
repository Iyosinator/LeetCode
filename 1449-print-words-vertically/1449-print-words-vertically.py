class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(len(word) for word in words)
        
        result = []
        for i in range(max_len):
            column = ''.join(word[i] if i < len(word) else ' ' for word in words)
            result.append(column.rstrip())
        
        return result
