class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            # check for duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = (-1)*nums[i]
            j = i+1
            k = len(nums)-1
            
            while j < k:
                s = nums[j] + nums[k]
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1
                elif s == target:
                    result.append([nums[i], nums[j], nums[k]])
                    # check for duplicates
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1

                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
        return result
