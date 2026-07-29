# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            # find kth node
            kth = groupPrev
            for i in range(k):
                kth = kth.next
                if kth == None:
                    return dummy.next

            groupNext = kth.next
            groupStart = groupPrev.next

            # reverse group
            pre = groupNext
            cur = groupStart
            for i in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur   # points to head of reversed
                cur = nxt
            
            # reconnect to previous group
            groupPrev.next = pre
            # move to next group (groupStart is now the end)
            groupPrev = groupStart