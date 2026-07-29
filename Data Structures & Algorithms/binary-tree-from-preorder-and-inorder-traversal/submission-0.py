# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # root node is first node of preorder array
        # finding root node in inorder array splits into two halves
        # use hash map for easy access, but what should the key value pairings be?
        # process
        # find root node from first thing in preorder arrray
        # use root node to partition inorder array into two
        # find "root" node again for left half and right half
        # where to define preIndex
        # how to know how much to increment preIndex by? is it just one?
        my_dict = {}
        preIndex = 0
        for i in range(len(inorder)):
            my_dict[inorder[i]] = i
        def build(left, right):
            nonlocal preIndex
            if left > right:
                return None
            root = TreeNode(preorder[preIndex])
            preIndex += 1
            idx = my_dict[root.val]
            root.left = build(left, idx - 1)
            root.right = build(idx + 1, right)
            return root
        return build(0, len(inorder)-1)