class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        for i in nums:
            res ^= i
        res ^= k
        tem = 0
        while res > 0:
            if (res & 1) != 0:
                tem += 1
            res >>= 1
        return tem
