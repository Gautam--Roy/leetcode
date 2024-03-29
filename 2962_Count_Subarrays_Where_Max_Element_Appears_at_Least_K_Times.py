class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        maxnum = max(nums)
        maxfreq = 0

        for r in range(len(nums)):
            if nums[r] == maxnum:
                maxfreq += 1
            while maxfreq == k:
                if nums[l] == maxnum:
                    maxfreq -= 1
                l += 1
            res += l
        return res
