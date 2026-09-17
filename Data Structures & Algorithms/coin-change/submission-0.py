class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) # dp[i] store min coins needed to make i
        dp[0] = 0 # base case, need 0 coins to make 0
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0: # check if coin fits
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        if dp[amount] != amount + 1:
            return dp[amount]
        return -1