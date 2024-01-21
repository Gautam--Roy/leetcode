class Solution:
    def isMonotonic(self, nums: [int]) -> bool:
        # if len(nums) == 1:
        #     return True

        numsLen = len(nums) - 1

        def checkEquals():
            for n in range(numsLen):
                if nums[n] != nums[n + 1]:
                    return False
            return True

        if checkEquals():
            return True

        def increasingMono():
            for n in range(numsLen):
                if nums[n + 1] - nums[n] >= 0:
                    continue
                else:
                    return False
            return True

        def decreasingMono():
            for n in range(numsLen):
                if nums[n + 1] - nums[n] <= 0:
                    continue
                else:
                    return False
            return True

        if increasingMono() or decreasingMono():
            return True
        return False


result = Solution().isMonotonic([1, 3, 2, 4])
print(result)
