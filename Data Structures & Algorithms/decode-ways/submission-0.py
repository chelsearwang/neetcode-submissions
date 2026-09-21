class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] = number of ways to decode the first i characters of the string
        dp = [0] * (len(s) + 1)
        dp[0] = 1

        # first char cannot be 0
        if s[0] != '0':
            dp[1] = 1
            
        for i in range(2, len(s)+1):
            ways = 0
            # take one digit
            if s[i-1] != '0':
                ways += dp[i-1]
            # take two digits
            if 10 <= int(s[i-2:i]) <= 26:
                ways += dp[i-2]
            dp[i] = ways
        return dp[len(s)]