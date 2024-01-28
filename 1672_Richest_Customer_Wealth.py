class Solution:
    def maximumWealth(self, accounts: [int]) -> int:
        tw = 0
        for account in accounts:
            if sum(account) >= tw: tw = sum(account)
        return tw
    
    
result = Solution().maximumWealth([[1,2,3],[3,2,1]])
print(result)