class Solution:
    def climbStairs(self, n: int) -> int:
        prev1 = 1
        prev2 = 2
        if n == 1:
            return prev1
        if n == 2:
            return prev2
        for i in range(3, n+1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr
        return curr
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