from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        answer = []
        l = 0
        for r in range(len(nums)):
            if r - l + 1 > k:
                l += 1
            # 1. Remove expired indices
            if q and q[0] < l:
                q.popleft()
            # 2. Remove smaller values from back
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            # 3. Append r
            q.append(r)
            if r - l + 1 == k:
                answer.append(nums[q[0]])
        return answer