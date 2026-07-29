# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # case 1: include both left and right subtrees
            # cannot return this path upwards, or else too many connections
        # case 2: include either left or right subtree
        # case 3: include no subtree
        max_sum = root.val # max sum can be negative!! so don't initialize to 0
        def dfs(node):
            nonlocal max_sum
            if node is None:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            max_sum = max(max_sum, node.val + left + right)
            return node.val + max(left, right)
        dfs(root)
        return max_sum