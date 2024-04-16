# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)

        def trav(node, depth_left):
            if node is None:
                return

            if depth_left == 1:
                oldl = node.left
                oldr = node.right

                node.left = TreeNode(val, oldl)
                node.right = TreeNode(val, right=oldr)

                return
            trav(node.left, depth_left - 1)
            trav(node.right, depth_left - 1)

        trav(root, depth - 1)
        return root
