class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(0, n):
            if nums[i] < 0 and abs(nums[i]) in nums:
                return abs(nums[i])
        return -1
