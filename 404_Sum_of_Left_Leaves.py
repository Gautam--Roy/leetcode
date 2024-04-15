# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def checkNode(node, isLeft):
            if not node:
                return 0
            if not node.left and not node.right and isLeft:
                return node.val
            return checkNode(node.left, True) + checkNode(node.right, False)

        return checkNode(root, False)
