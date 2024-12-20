# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
    
        queue = deque([root])
        is_odd_level = False
        while queue:
            level_size = len(queue)
            current_level_nodes = []
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                current_level_nodes.append(node)
            if is_odd_level:
                left, right = 0, len(current_level_nodes) - 1
                while left < right:
                    current_level_nodes[left].val, current_level_nodes[right].val = \
                        current_level_nodes[right].val, current_level_nodes[left].val
                    left += 1
                    right -= 1
            is_odd_level = not is_odd_level
        return root
