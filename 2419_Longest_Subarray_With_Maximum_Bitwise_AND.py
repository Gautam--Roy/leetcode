class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans, count = 0,0
        mx = max(nums)
        for i in nums:
            if i == mx:
                count += 1
            else:
                count = 0
            ans = max(ans, count)
        return ans
