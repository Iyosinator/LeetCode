class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases: if n is 1 or 2, return n directly
        if n <= 2:
            return n
        
        # Initialize DP array to store the number of ways to reach each step
        dp = [0] * (n + 1)
        
        # Base cases: the number of ways to reach step 1 and step 2
        dp[1] = 1
        dp[2] = 2
        
        # Fill the DP table using the recurrence relation
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        # Return the result for n steps
        return dp[n]
