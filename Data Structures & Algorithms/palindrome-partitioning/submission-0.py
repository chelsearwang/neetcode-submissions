class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        substrings = []
        def isPalindrome(st):
            st_len = len(st)
            for i in range(0, st_len//2):
                if st[i] != st[st_len-1-i]:
                    return False
            return True
        def backtrack(start):
            if start == len(s):
                result.append(substrings[:])
                return
            for i in range(start, len(s)):
                if isPalindrome(s[start:i+1]):
                    palindrome = s[start:i+1]
                    substrings.append(palindrome)
                    backtrack(i + 1)
                    substrings.pop()

        backtrack(0)
        return result