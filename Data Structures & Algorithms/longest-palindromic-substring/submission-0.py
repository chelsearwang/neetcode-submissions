class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        start = 0
        max_len = 1

        for length in range(1, n + 1): # loop from smaller length vals first
            for i in range(n - length + 1):
                j = i + length - 1 # i & j are substr bounds

                if length == 1:
                    dp[i][j] = True
                elif length == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

                if dp[i][j] and length > max_len:
                    start = i
                    max_len = length

        return s[start:start + max_len]