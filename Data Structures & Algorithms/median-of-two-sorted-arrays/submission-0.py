class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp
        l1 = len(nums1)
        l2 = len(nums2)
        left_size = (l1 + l2 + 1) // 2
        left = 0
        right = l1
        partition1 = 0
        while left <= right:
            p1 = (left + right) // 2    # num elements for left half
            p2 = left_size - p1
            if p1 == 0:
                nums1_left = -float("inf")
            else:
                nums1_left = nums1[p1-1]
            if p1 == l1:
                nums1_right = float("inf")
            else:
                nums1_right = nums1[p1]
            if p2 == 0:
                nums2_left = -float("inf")
            else:
                nums2_left = nums2[p2-1]
            if p2 == l2:
                nums2_right = float("inf")
            else:
                nums2_right = nums2[p2]
            # print(nums1_left, nums1_right, nums2_left, nums2_right)
            if nums1_left > nums2_right:
                right = p1 - 1
            elif nums2_left > nums1_right:
                left = p1 + 1
            elif (nums1_left <= nums2_right) and (nums2_left <= nums1_right):
                left_max = max(nums1_left, nums2_left)
                right_min = min(nums1_right, nums2_right)
                if (l1 + l2) % 2 == 0:
                    return (left_max + right_min) / 2
                else:
                    return left_max