class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(len(s)):
            # ddd-len palindrome
            odd = expand(i, i)
            # even-len palindrome
            even = expand(i, i + 1)
            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even

        return result

        """
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
        """