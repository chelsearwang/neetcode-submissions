class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        cur_len = 0
        my_set = set()
        l = 0
        r = 0
        while r < len(s):
            if s[r] in my_set:
                while s[l] != s[r]:
                    my_set.remove(s[l])
                    l += 1
                l += 1
            else:
                my_set.add(s[r])
            cur_len = r - l + 1
            max_len = max(cur_len, max_len)
            r += 1
        return max_len