# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        def mergeTwoLists(l1, l2):
            dummy = ListNode()
            cur = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            if l1:
                cur.next = l1
            else:
                cur.next = l2
            return dummy.next
        
        while len(lists) > 1:
            merged = []
            # merge pairs of lists
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(mergeTwoLists(l1, l2))
            lists = merged
        return lists[0]
        """
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
        """