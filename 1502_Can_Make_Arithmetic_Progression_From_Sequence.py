class Solution:
    def canMakeArithmeticProgression(self, arr: [int]) -> bool:
        newArray = sorted(arr)
        i = 0
        while i <= len(newArray) - 3:
            if newArray[i + 1] - newArray[i] != newArray[i + 2] - newArray[i + 1]:
                return False
            i += 1
        return True


result = Solution().canMakeArithmeticProgression([1, 2, 4])
print(result)
