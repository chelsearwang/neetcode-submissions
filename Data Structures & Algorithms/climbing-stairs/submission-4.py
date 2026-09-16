class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev1 = 1
        prev2 = 2

        for i in range(3, n+1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr

        return prev2

        """
        dp = [0] * (n + 1)
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
        """