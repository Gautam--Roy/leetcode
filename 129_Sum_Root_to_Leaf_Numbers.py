# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def calnum(node, pos):
            if node:
                if not node.left and not node.right:  # leaf
                    return pos * 10 + node.val
                sum = 0
                sum += calnum(node.left, pos * 10 + node.val)
                sum += calnum(node.right, pos * 10 + node.val)
                return sum
            else:
                return 0

        return calnum(root, 0)
