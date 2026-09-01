class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        subset = []
        def backtrack(i):
            result.append(subset[:])
            for j in range(i, len(nums)):
                num = nums[j]
                if j > i and nums[j] == nums[j-1]:
                    continue

                subset.append(num)
                backtrack(j+1)
                subset.pop()

        backtrack(0)
        return result