class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        ans = 0
        l = 0
        prod = 1

        for r in range(len(nums)):
            prod *= nums[r]

            if prod >= k:
                while prod >= k and l <= r:
                    prod /= nums[l]
                    l += 1
            ans += r - l + 1
        return ans
