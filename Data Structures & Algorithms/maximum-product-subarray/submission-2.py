class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_max = nums[0]
        prev_min = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]

            curr_max = max(n, n * prev_max, n * prev_min)

            curr_min = min(n, n * prev_max, n * prev_min)

            prev_max = curr_max
            prev_min = curr_min

            result = max(result, curr_max)
        return result
        """
        max_dp = [nums[0]] * len(nums)
        min_dp = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            n = nums[i]
            max_dp[i] = max(n, n*max_dp[i-1], n*min_dp[i-1])
            min_dp[i] = min(n, n*max_dp[i-1], n*min_dp[i-1])
        # print(max_dp)
        # print(min_dp)
        max_num = max(max_dp)
        # min_num = max(min_dp)
        # return max(max_num, min_num)
        return max_num
        """