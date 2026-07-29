class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        # find intersection point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        # slow and fast can equal at any point in the cycle
        # find cycle entrance
        # first intersectino point to start of cycle is always equal to first node and start of cycle
        slow2 = nums[0]

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow