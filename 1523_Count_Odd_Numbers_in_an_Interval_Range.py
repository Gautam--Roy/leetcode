class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if (low % 2 == 0 and high % 2 == 0):
            return int((high - low) / 2)
        return int((high - low) / 2 + 1)
    
result = Solution().countOdds(8, 10)
print(result)