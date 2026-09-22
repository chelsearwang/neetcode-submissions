class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] = can everthing before index i be segmented
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] == True:
                    needed_word = s[j:i]
                    if needed_word in wordDict:
                        dp[i] = True
                        break
        return dp[len(s)]