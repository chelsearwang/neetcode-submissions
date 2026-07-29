# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split list in half using fast and slow pointer approach
        # slow pointer will point to midpoint of list
        # reverse second half of list
        # merge two halves

        # find middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow now points to last element of first half
        # split list
        second = slow.next
        slow.next = None

        # reverse second half
        prev = None
        curr = second
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        # prev is now head of reverse half of list
        # merge two halves
        first = head
        second = prev
        while second:
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next
            first = first_next
            second = second_next
        # don't return, modify in place