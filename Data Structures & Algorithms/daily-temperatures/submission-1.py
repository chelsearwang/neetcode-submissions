from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        answer = [0] * len(temperatures)
        for t in range(len(temperatures)):
            if not stack or temperatures[t] <= temperatures[stack[-1]]:
                stack.append(t)
            else:
                while stack and temperatures[t] > temperatures[stack[-1]]:
                    low_index = stack.pop()
                    answer[low_index] = t-low_index
                stack.append(t)
        return answer