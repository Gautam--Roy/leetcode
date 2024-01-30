class Solution:
    def diagonalSum(self, mat: [int]) -> int:
        n = len(mat)
        sum = 0
        
        if n == 1:
            return mat[0][0]
        
        for i, l in enumerate(mat):
            if i == n-1 - i:
                sum += l[i]
            else:
                sum += l[i] + l[n-1 - i]
        return sum
result = Solution().diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]])
# result = Solution().diagonalSum([[4]])
print(result)