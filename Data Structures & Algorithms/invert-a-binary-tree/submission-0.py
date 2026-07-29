# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        cur = root
        temp = cur.right
        cur.right = cur.left
        cur.left = temp
        self.invertTree(cur.left)
        self.invertTree(cur.right)
        return root