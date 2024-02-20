class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = n * (n+1)/2
        check = 0
        for x in range(0 , n):
            check += nums[x]
        return int(sum - check)