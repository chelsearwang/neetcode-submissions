class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        f1 = [0] * 26
        f2 = [0] * 26
        for char in s1:
            f1[ord(char) - ord("a")] += 1
        l = 0
        r = len(s1) - 1
        for i in range(l, r+1):
            f2[ord(s2[i]) - ord("a")] += 1
        if (f1 == f2): 
            return True
        while (r < len(s2) - 1):
            f2[ord(s2[l]) - ord("a")] -= 1
            l += 1
            r += 1
            f2[ord(s2[r]) - ord("a")] += 1
            if (f1 == f2):
                return True
        return False