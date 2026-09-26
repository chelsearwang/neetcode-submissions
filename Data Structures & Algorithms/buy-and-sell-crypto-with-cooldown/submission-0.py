class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0 - hold, 1 - sell, 2 - cooldown
        dp = [[0 for _ in range(3)] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = float("-inf")
        dp[0][2] = 0
        for i in range(1, len(prices)):
            price = prices[i]
            for j in range(3):
                if j == 0:      # hold (have coin)
                    dp[i][j] = max(dp[i-1][2] - price, dp[i-1][0])
                elif j == 1:    # sell
                    dp[i][j] = dp[i-1][0] + price
                else:           # cooldown/rest (no coin)
                    dp[i][j] = max(dp[i-1][1], dp[i-1][2])
        # print(dp)
        return max(dp[len(prices)-1])