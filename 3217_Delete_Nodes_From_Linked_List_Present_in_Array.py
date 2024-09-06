class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        mv = -1
        for num in nums:
            mv = max(num, mv)
        freq = [False] * (mv + 1)
        for num in nums:
            freq[num] = True
        temp = ListNode()
        current = temp
        while head:
            if head.val >= len(freq) or not freq[head.val]:
                current.next = head
                current = current.next
            head = head.next
        current.next = None
        return temp.next
