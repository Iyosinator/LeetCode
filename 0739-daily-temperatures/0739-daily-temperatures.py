class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0] * n

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev_day = stack.pop()
                ans[prev_day] = i - prev_day
            stack.append(i)
        return ans

