import collections


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        counts = collections.Counter(nums)
        mx = max(counts.values())
        
        freq = 0
        for x in nums:
            if counts[x] == mx:
                freq += 1
        
        
        return freq


result = Solution().maxFrequencyElements([1,2,2,3,1,4,5])
print(result)

