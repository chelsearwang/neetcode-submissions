from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        open_paren = {"{", "(", "["}
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for char in s:
            if char in open_paren:
                stack.append(char)
            else:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
        return not stack