class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarratmostk(k):
            n = len(nums)
            hmap = collections.Counter()
            ans, d = 0, 0
            l, r = 0, 0
            for i in range(n):
                if nums[i] not in hmap:
                    d += 1
                while l <= r and d > k:
                    hmap[nums[l]] -= 1
                    if hmap[nums[l]] == 0:
                        d -= 1
                        del hmap[nums[l]]
                    l += 1
                ans += r - l + 1
                hmap[nums[i]] += 1
                r += 1
            return ans

        ans1 = subarratmostk(k)
        ans2 = subarratmostk(k - 1)
        return ans1 - ans2
