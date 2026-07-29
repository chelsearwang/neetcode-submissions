# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # start counting with root.left
        # count middle node
        # count root.right
        count = 0
        answer = 0
        def dfs(root):
            nonlocal count, answer
            if root is None:
                return
            dfs(root.left)
            count += 1
            if count == k:
                answer = root.val
                return
            dfs(root.right)
        dfs(root)
        return answer