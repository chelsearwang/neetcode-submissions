class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        combo = []
        candidates.sort() # for detecting consecutive duplicates
        def backtrack(i, s):
            if s == target:
                result.append(combo[:])
                return

            for j in range(i, len(candidates)):
                if candidates[j] + s > target:
                    break
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                combo.append(candidates[j])
                backtrack(j+1, s + candidates[j])
                combo.pop()
        backtrack(0, 0)
        return result