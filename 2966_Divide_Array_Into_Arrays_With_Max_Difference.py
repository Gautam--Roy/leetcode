class Solution:
    def divideArray(self, nums: [int], k: int) -> [[int]]:
        sortedArr = sorted(nums)
        ans = []
        for oc in range(0, len(sortedArr), 3):
            if sortedArr[oc + 2] - sortedArr[oc] <= k:
                ans.append(sortedArr[oc : oc + 3])
        if len(ans) != len(sortedArr) / 3 : return []
        else: return ans
result = Solution().divideArray([33,26,4,18,16,24,24,15,8,18,34,20,24,16,3], 16)
print(result)