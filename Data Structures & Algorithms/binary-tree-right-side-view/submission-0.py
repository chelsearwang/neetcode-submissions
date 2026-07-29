# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = deque()
        if root is None:
            return result
        q.append(root)
        while q:
            # level order traversal but always put rightmost node first
            level_len = len(q)
            first = True
            for i in range(level_len):
                node = q.popleft()
                if first:
                    result.append(node.val)
                    first = False
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return result