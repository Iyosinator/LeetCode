class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = []
        num_str = str(num)
        changed = False

        for i in range(len(num_str)):
            if (num_str[i] == "6") and not changed:
                ans.append("9")
                changed = True
            else:
                ans.append(num_str[i])

        return int(''.join(ans))



        