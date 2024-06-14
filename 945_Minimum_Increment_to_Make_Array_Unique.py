class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        inc = 0
        trk = 0

        for i in nums:
            trk = max(i, trk)
            inc += trk - i
            trk += 1
        return inc
