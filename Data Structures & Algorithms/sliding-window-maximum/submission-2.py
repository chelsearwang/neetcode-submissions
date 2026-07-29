from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        answer = []
        l = 0
        for r in range(len(nums)):
            # check if need to slide left
            if r - l + 1 > k:
                l += 1
            # remove max if shifted out of window
            while q and q[0] < l:
                q.popleft()
            # remove smaller values from back
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if r - l + 1 == k:
                answer.append(nums[q[0]])
        return answer