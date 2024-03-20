# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        edgeNodes = []
        dummy = ListNode()
        head1 = list1
        dummy.next = head1
        count = 0
        while head1:
            if count == a - 1 or count == b + 1:
                edgeNodes.append(head1)
            count += 1
            head1 = head1.next
        edgeNodes[0].next = list2
        while list2.next != None:
            list2 = list2.next
        list2.next = edgeNodes[1]

        return dummy.next
