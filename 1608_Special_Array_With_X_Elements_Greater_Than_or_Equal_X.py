class Solution:
    def specialArray(self, nums: list[int]) -> int:
        n: int = len(nums)
        freq = [0 for _ in range(n + 1)]

        for num in nums:
            freq[min(n, num)] += 1

        greaterOrequalCount = 0
        for num in range(n, 0, -1):
            greaterOrequalCount += freq[num]
            if num == greaterOrequalCount:
                return num

        return -1
