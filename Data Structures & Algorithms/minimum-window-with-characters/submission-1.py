class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        # get frequency of chars in t string
        freq_t = {}
        for char in t:
            if char in freq_t:
                freq_t[char] += 1
            else:
                freq_t[char] = 1

        # set up sliding window
        l = 0 
        freq_s = {}
        best_len = float("inf")
        best_l = 0
        best_r = 0
        count = 0 # track num unique chars included
        for r in range(len(s)):
            char = s[r]
            if char in freq_s:
                freq_s[char] += 1
            else:
                freq_s[char] = 1
            if char in freq_t:
                if freq_s[char] == freq_t[char]:
                    count += 1
            # check if window is valid
            len_t = len(freq_t)
            while count == len_t:
                # possibly update answer
                window_len = r - l + 1
                if window_len < best_len:
                    best_len = window_len
                    best_l = l
                    best_r = r
                # try shrinking window
                ch_removed = s[l]
                freq_s[ch_removed] -= 1
                if ch_removed in freq_t and freq_s[ch_removed] < freq_t[ch_removed]:
                    count -= 1
                l += 1
        if best_len == float("inf"):
            return ""
        return s[best_l:best_r+1]