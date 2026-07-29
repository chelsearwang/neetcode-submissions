# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # when going down tree, keep track of max seen value
        def dfs(node, maxSoFar):
            if node is None:
                return 0
            newMax = max(node.val, maxSoFar)
            left = dfs(node.left, newMax)
            right = dfs(node.right, newMax)
            if node.val >= maxSoFar:
                return 1 + left + right
            return left + right
        return dfs(root, root.val)