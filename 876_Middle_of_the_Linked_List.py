# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # add = []
        # h = head

        # while h:
        #     add.append(h)
        #     h = h.next
        # n = len(add)
        # return add[n//2]

        # Another solution is to race the 2 pointers. Move the fast as 2 nodes at once. Fast will reach the end, the slow will be at the middle.
        s = head
        f = head
        while f and f.next:
            s = s.next
            f = f.next.next
        return s
