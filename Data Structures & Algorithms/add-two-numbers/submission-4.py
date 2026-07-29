# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        dummy = ListNode()
        p = dummy
        carry = 0
        while curr1 or curr2:
            x = curr1.val if curr1 else 0
            y = curr2.val if curr2 else 0
            pure_sum = x + y + carry
            digit_sum = pure_sum % 10
            carry = pure_sum // 10
            p.next = ListNode(digit_sum)
            p = p.next
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        if carry > 0:
            p.next = ListNode(carry)
        return dummy.next