# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        arr = []
        dum = head
        while dum:
            arr.append(dum)
            dum = dum.next

        i, l = 0, len(arr) - 1

        head = arr[0]

        while i != l:
            arr[i].next = arr[l]
            i += 1
            if l - i == 1 or l == i:
                arr[l].next = arr[i]
                arr[i].next = None
                break
            arr[l].next = arr[i]
            l -= 1
