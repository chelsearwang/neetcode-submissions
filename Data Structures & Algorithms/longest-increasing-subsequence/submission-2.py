class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = length of the longest increasing subsequence that ends at index i
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        # print(dp)
        return max(dp)