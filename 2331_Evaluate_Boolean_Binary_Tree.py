# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self, root):
        if root.val == 0 or root.val == 1:
            return root.val == 1
        elif root.val == 2:
            return self.rec(root.left) or self.rec(root.right)
        elif root.val == 3:
            return self.rec(root.left) and self.rec(root.right)
        return False

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return self.rec(root)
