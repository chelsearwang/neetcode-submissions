class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_dp = [nums[0]] * len(nums)
        min_dp = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            n = nums[i]
            max_dp[i] = max(n, n*max_dp[i-1], n*min_dp[i-1])
            min_dp[i] = min(n, n*max_dp[i-1], n*min_dp[i-1])
        # print(max_dp)
        # print(min_dp)
        max_num = max(max_dp)
        min_num = max(min_dp)
        return max(max_num, min_num)