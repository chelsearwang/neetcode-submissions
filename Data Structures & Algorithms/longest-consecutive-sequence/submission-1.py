class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in set_nums: # start of new sequence
                current = 0
                # print("start: " + str(num))
                number = num
                while number in set_nums:
                    current += 1
                    number += 1
                longest = max(current, longest)
        return longest
        