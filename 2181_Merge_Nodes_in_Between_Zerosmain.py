# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        pointer = head.next
        sum = 0
        while pointer.val != 0:
            sum += pointer.val
            pointer = pointer.next
        head.next.val = sum
        head.next.next = self.mergeNodes(pointer)
        return head.next
