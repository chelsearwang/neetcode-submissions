class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        for char in s:
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 1
        for char in t:
            if char in my_dict:
                my_dict[char] -= 1
            else:
                return False

        for key in my_dict:
            if my_dict[key] != 0:
                return False
        return True