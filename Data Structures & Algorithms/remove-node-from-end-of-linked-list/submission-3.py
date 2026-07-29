# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        p1 = dummy
        p2 = dummy
        for i in range(n+1):
            p2 = p2.next
        while p2:
            p2 = p2.next
            p1 = p1.next
        # p1 now points to prev node
        prev = p1
        curr = prev.next
        next_node = prev.next.next
        curr.next = None
        prev.next = next_node
        return dummy.next
        """
        len_list = 0
        curr = head
        while curr:
            len_list += 1
            curr = curr.next
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
        """
        