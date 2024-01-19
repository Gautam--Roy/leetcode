class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        switcher = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[switcher], nums[i] = nums[i], nums[switcher]
                switcher += 1


result = Solution().moveZeroes([1, 0, 12, 0, 5, 0, 13, 5, 0, 5, 1, 0])
