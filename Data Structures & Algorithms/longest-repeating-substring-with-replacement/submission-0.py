class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        my_dict = {}
        l = 0
        r = 0
        while r < len(s):
            if s[r] in my_dict:
                my_dict[s[r]] += 1
            else:
                my_dict[s[r]] = 1
            max_frequency = max(my_dict.values())
            window_len = r - l + 1
            num_replacements = window_len - max_frequency
            if num_replacements > k:
                while window_len - max_frequency > k:
                    my_dict[s[l]] -= 1
                    l += 1
                    window_len = r - l + 1
                    max_frequency = max(my_dict.values())
            max_len = max(window_len, max_len)
            r += 1
        return max_len