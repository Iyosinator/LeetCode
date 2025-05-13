class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    result.append(".".join(path))
                return
            
            for end in range(start + 1, min(start + 4, len(s) + 1)):
                part = s[start:end]
                if (part[0] == '0' and len(part) > 1) or int(part) > 255:
                    continue
                backtrack(end, path + [part])
    
        result = []
        backtrack(0, [])
        return result
        