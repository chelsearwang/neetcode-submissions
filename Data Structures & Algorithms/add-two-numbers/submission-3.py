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
        while curr1 and curr2:
            pure_sum = curr1.val + curr2.val + carry
            digit_sum = pure_sum % 10
            carry = pure_sum // 10
            p.next = ListNode(digit_sum)
            p = p.next
            curr1 = curr1.next
            curr2 = curr2.next
        while curr1:
            digit_sum = (curr1.val + carry) % 10
            carry = (curr1.val + carry) // 10
            p.next = ListNode(digit_sum)
            p = p.next
            curr1 = curr1.next
        while curr2:
            digit_sum = (curr2.val + carry) % 10
            carry = (curr2.val + carry) // 10
            p.next = ListNode(digit_sum)
            p = p.next
            curr2 = curr2.next
        if carry > 0:
            p.next = ListNode(carry)
        return dummy.next