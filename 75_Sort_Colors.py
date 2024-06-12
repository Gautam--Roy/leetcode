class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r, w, b = 0, 0, 0
        for i in nums:
            if i == 0:
                r += 1
            elif i == 1:
                w += 1
            else:
                b += 1
        for i in range(len(nums)):
            if i < r:
                nums[i] = 0
            elif i < r + w:
                nums[i] = 1
            else:
                nums[i] = 2
