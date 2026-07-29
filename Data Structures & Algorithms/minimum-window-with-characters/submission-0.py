class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        # get frequency of chars in t string
        ft = {}
        for char in t:
            if char in ft:
                ft[char] += 1
            else:
                ft[char] = 1

        l = 0   # left pointer in sliding window
        st = {}
        best_length = float("inf")
        best_l = 0
        best_r = 0
        formed = 0  # track num of chars that are met
        for r in range(len(s)):
            char = s[r]
            if char in st:
                st[char] += 1
            else:
                st[char] = 1
            if char in ft:
                if st[char] == ft[char]:
                    formed += 1
            # check if window is valid
            while formed == len(ft):
                window_len = r - l + 1
                if window_len < best_length:
                    best_length = window_len
                    best_l = l
                    best_r = r
                # try shrinking
                ch_removed = s[l]
                st[ch_removed] -= 1
                if ch_removed in ft and st[ch_removed] < ft[ch_removed]:
                    formed -= 1
                l += 1
        if best_length == float("inf"):
            return ""
        return s[best_l:best_r+1]