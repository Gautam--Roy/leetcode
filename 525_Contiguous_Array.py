class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        s = {}
        s[0] = -1
        count = 0
        mx = 0

        for i in range(len(nums)):
            count += 1 if nums[i] else -1

            if count in s:
                mx = max(mx, i - s[count])
            else:
                s[count] = i

        return mx
