class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        max_frequency = 0
        my_dict = {}
        l = 0
        r = 0
        while r < len(s):
            if s[r] in my_dict:
                my_dict[s[r]] += 1
            else:
                my_dict[s[r]] = 1
            max_frequency = max_frequency = max(max_frequency, my_dict[s[r]])
            window_len = r - l + 1
            num_replacements = window_len - max_frequency
            while window_len - max_frequency > k:
                my_dict[s[l]] -= 1
                l += 1
                window_len = r - l + 1
            max_len = max(r-l+1, max_len)
            r += 1
        return max_len