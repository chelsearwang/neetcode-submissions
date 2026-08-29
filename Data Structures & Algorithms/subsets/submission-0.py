class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # two options for each num: include or dont
        result = []
        subset = []
        def dfs(i):
            if i == len(nums):
                result.append(subset[:])
                return
            # include num and recurse
            subset.append(nums[i])
            dfs(i+1)
            # backtrack and recurse
            subset.pop()
            dfs(i+1)
        dfs(0)
        return result