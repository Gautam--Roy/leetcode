# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        node = head
        grt = self.removeNodes(node.next)

        node.next = grt
        if not grt or node.val >= grt.val:
            return node
        return grt
