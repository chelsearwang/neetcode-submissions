"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
       
        # first pass: create new nodes
        curr = head
        my_dict = {}
        while curr:
            my_dict[curr] = Node(curr.val)
            curr = curr.next
        
        # second pass: connect next and random pointers
        curr = head
        while curr:
            copy = my_dict[curr]
            if curr.next:
                copy.next = my_dict[curr.next]
            else:
                copy.next = None

            if curr.random:
                copy.random = my_dict[curr.random]
            else:
                copy.random = None 
            curr = curr.next
        return my_dict[head]