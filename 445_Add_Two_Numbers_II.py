# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        n1, n2 = 0, 0

        while l1:
            n1 = (n1 * 10) + l1.val
            l1 = l1.next
        while l2:
            n2 = (n2 * 10) + l2.val
            l2 = l2.next

        num = str(n1 + n2)

        dm = dumNode = ListNode(0)
        for x in num:
            nn = ListNode(x)
            dm.next = nn
            dm = dm.next
        return dumNode.next
