# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            fast = fast.next
            if slow == fast:
                return True
        return False
        """
        visited_nodes = set()
        current = head
    
        while current:
            if current in visited_nodes:
                return True           # node already visited, cycle exists
            visited_nodes.add(current)
            current = current.next
            
        return False 
        """