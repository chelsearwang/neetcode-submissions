# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_list = 0
        curr = head
        while curr:
            len_list += 1
            curr = curr.next
        print(len_list)
        if len_list == 1:
            return None
        prev = head
        i = len_list - n
        if i-1 < 0:
            return head.next
        while i-1 > 0:
            prev = prev.next
            i -= 1
        # prev points to node right before one removed
        curr = prev.next
        next_node = prev.next.next
        curr.next = None
        prev.next = next_node
        return head
        