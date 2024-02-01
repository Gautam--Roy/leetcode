class Solution:
    def average(self, salary: [int]) -> float:
        sortedSal = sorted(salary)
        del sortedSal[0]
        del sortedSal[-1]
        return sum(sortedSal) / len(sortedSal)
    
result = Solution().average([4000,3000,1000,2000])
print(result)