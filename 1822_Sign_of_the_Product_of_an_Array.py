class Solution:
    def arraySign(self, nums: [int]) -> int:
        product = 1
        for n in nums:
            product *= n
        if product == 0:
            return 0
        if product > 0:
            return 1
        return -1
