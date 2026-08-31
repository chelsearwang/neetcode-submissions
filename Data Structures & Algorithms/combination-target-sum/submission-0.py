class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        combo = []
        def backtrack(i, s):
            if s == target:
                result.append(combo[:])
                return
            for j in range(i, len(nums)):
                new_sum = s + nums[j]
                if new_sum > target:
                    continue
                combo.append(nums[j])
                backtrack(j, new_sum)
                combo.pop()
        backtrack(0, 0)
        return result