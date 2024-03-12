# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = ListNode()
        # t = dummy
        # f = head
        # s = head.next

        # while f and s.next:
        #     print(f.val)
        #     print(s.val)
        #     if f.val + s.val == 0:
        #         f = f.next.next
        #         s = s.next.next
        #     else :
        #         t.next = f
        #         f = f.next
        #         s = s.next
        # return dummy.next

        dummy = ListNode(0)
        dummy.next = head
        prefixSumToNode = {}
        prefixSum = 0
        current = dummy
        while current:
            prefixSum += current.val
            if prefixSum in prefixSumToNode:
                prev = prefixSumToNode[prefixSum]
                toRemove = prev.next
                p = prefixSum + (toRemove.val if toRemove else 0)
                while p != prefixSum:
                    del prefixSumToNode[p]
                    toRemove = toRemove.next
                    p += toRemove.val if toRemove else 0
                prev.next = current.next
            else:
                prefixSumToNode[prefixSum] = current
            current = current.next
        return dummy.next
