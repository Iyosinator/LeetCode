class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block = False
        result = []
        buffer = []
        
        for line in source:
            i = 0
            while i < len(line):
                if not in_block and i + 1 < len(line) and line[i:i+2] == "/*":
                    in_block = True
                    i += 1
                elif in_block and i + 1 < len(line) and line[i:i+2] == "*/":
                    in_block = False
                    i += 1
                elif not in_block and i + 1 < len(line) and line[i:i+2] == "//":
                    break
                elif not in_block:
                    buffer.append(line[i])
                i += 1
            
            if not in_block and buffer:
                result.append("".join(buffer))
                buffer = []
                
        return result
