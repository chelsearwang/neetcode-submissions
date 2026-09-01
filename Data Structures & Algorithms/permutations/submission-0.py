class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []
        used = set()

        def backtrack():
            if len(perm) == len(nums):
                result.append(perm[:])
                return
                
            for i in range(len(nums)):
                num = nums[i]

                if num in used:
                    continue

                used.add(num)
                perm.append(num)

                backtrack()

                used.remove(num)
                perm.pop()

        backtrack()
        return result