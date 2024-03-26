class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nm = {}
        mx = max(nums, default=0)
        for num in nums:
            nm[num] = True
        for i in range(1, mx):
            if i not in nm:
                return i
        return 1 if mx < 0 else mx + 1
