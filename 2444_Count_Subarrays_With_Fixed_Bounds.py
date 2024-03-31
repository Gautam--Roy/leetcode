class Solution:
    def countSubarrays(self, nums: List[int], mink: int, maxK: int) -> int:

        ans = 0
        badIndex = leftIndex = rightIndex = -1

        for i, num in enumerate(nums) :
            if not mink <= num <= maxK:
                badIndex = i

            if num == mink:
                leftIndex = i

            if num == maxK:
                rightIndex = i

            ans += max(0, min(leftIndex, rightIndex) - badIndex)

        return ans