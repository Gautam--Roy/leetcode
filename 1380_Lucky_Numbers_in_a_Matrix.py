class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans = []
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            rmin = min(matrix[i])
            rmindex = matrix[i].index(rmin)

            lc = True
            for j in range(n):
                if matrix[j][rmindex] > rmin:
                    lc = False
                    break
            if lc:
                ans.append(rmin)
        return ans
