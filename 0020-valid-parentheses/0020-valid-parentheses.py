class Solution:
    def isValid(self, s: str) -> bool:
        def helper(start, end):
            if start > end:
                return True
            if (end - start + 1) % 2 != 0:
                return False

            pairs = {'(': ')', '[': ']', '{': '}'}

            if s[start] not in pairs:
                return False

            match = pairs[s[start]]
            depth = 0

            for i in range(start + 1, end + 1):
                if s[i] == s[start]:
                    depth += 1
                elif s[i] == match:
                    if depth == 0:
                        return helper(start + 1, i - 1) and helper(i + 1, end)
                    else:
                        depth -= 1
            return False

        return helper(0, len(s) - 1)
