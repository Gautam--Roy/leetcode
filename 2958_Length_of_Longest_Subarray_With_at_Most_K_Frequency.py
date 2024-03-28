class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        hmap = defaultdict(int)

        for r in range(len(nums)):
            hmap[nums[r]] += 1

            while hmap[nums[r]] > k:
                hmap[nums[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res
