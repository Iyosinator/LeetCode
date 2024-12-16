class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brac_dict = {
            ")":"(",
            "}":"{",
            "]":"["

        }
        for char in s:
            if char in brac_dict:
                if stack and stack[-1] == brac_dict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack            

         
        