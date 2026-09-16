class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[n-1]
        prev1 = nums[0]
        prev2 = max(nums[0], nums[1])
        for i in range(2, n):
            curr = max(prev1 + nums[i], prev2)
            prev1 = prev2
            prev2 = curr
        return prev2
        """
        n = len(nums)
        dp = [0] * n
        if n < 2:
            return nums[n-1]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        # print(dp)
        return dp[n-1]
        """