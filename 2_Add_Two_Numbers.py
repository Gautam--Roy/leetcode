# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode(0)
        tail = head
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            newNode = ListNode(val)
            tail.next = newNode
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        result = head.next
        head.next = None
        return result
result = Solution().addTwoNumbers([2, 4, 3], [5, 6, 4])
print(result)
# testing the new feature using git stash
