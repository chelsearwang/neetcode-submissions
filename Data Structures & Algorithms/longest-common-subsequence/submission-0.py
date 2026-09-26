class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        i = len(text1)
        j = len(text2)
        dp = [[0 for _ in range(j+1)] for _ in range(i+1)]

        for row in range(1, i + 1):
            for col in range(1, j + 1):
                if text1[row - 1] == text2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

        return dp[i][j]