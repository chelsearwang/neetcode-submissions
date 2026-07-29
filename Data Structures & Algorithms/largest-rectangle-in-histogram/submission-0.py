from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1] * n
        right = [n] * n
        
        # LEFT boundary
        stack = deque()
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        # RIGHT boundary
        stack = deque()
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        # compute answer
        ans = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            ans = max(ans, heights[i] * width)

        return ans

