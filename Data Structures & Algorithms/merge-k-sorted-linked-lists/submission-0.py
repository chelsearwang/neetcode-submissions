# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        for i in range(1, len(lists)):
            list1 = lists[i-1]
            list2 = lists[i]
            dummy = ListNode()
            head = dummy
            while list1 and list2:
                if list1.val > list2.val:
                    head.next = list2
                    list2 = list2.next
                else:
                    head.next = list1
                    list1 = list1.next
                head = head.next
            if list1:
                head.next = list1
            else:
                head.next = list2
            lists[i] = dummy.next
        return lists[-1]