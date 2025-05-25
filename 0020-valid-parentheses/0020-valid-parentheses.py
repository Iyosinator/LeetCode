class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brac_dict = { ")":"(", "}":"{", "]":"[" }
        opening = set(brac_dict.values())

        for char in s:
            if char in brac_dict.keys():
                if stack and stack[-1] == brac_dict[char]:
                    stack.pop()
                else:
                    return False
            elif char in opening:
                stack.append(char)
            else:
                continue
        return not stack            

         
        