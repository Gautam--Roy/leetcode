class Solution:
    def largestPerimeter(self, nums: [int]) -> int:
        # Concept : Largest side of the triangle should be smaller than the sum other 2
        nums = sorted(nums)
        for i in range(len(nums) - 3, -1, -1):
            if nums[i+2] < nums[i+1] + nums[i]:
                return sum(nums[i: i+3])
        return 0
    
result = Solution().largestPerimeter([2,1,2])
print(result)
        