# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        values = []
        car = 0

        while head is not None:
            values.append(head.val)
            head = head.next

        tailn = None

        while values or car != 0:

            tailn = ListNode(0, tailn)

            if values:
                car += values.pop() * 2
            tailn.val = car % 10
            car //= 10

        return tailn
