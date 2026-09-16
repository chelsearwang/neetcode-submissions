class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(nums):
            prev2 = 0
            prev1 = 0

            for num in nums:
                curr = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = curr

            return prev1

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
        
        """
        n = len(nums)
        if n < 2:
            return nums[n-1]
        elif n == 2:
            return max(nums[0], nums[1])

        dp1 = [0] * (n-1)
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])

        dp2 = [0] * (n-1)
        dp2[0] = nums[1]
        dp2[1] = max(nums[1], nums[2])

        for i in range(2, n-1):
            dp1[i] = max(dp1[i-2] + nums[i], dp1[i-1])
            dp2[i] = max(dp2[i-2] + nums[i+1], dp2[i-1])
        
        return max(dp1[n-2], dp2[n-2])
        """
