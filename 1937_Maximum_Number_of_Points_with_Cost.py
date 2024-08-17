class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dpp = [0] * n
        for j in range(n):
            dpp[j] = points[0][j]
        for i in range(1, m):
            lMax = [0] * n
            rMax = [0] * n
            newDpp = [0] * n
            lMax[0] = dpp[0]
            for j in range(1, n):
                lMax[j] = max(lMax[j - 1], dpp[j] + j)
            rMax[n - 1] = dpp[n - 1] - (n - 1)
            for j in range(n - 2, -1, -1):
                rMax[j] = max(rMax[j + 1], dpp[j] - j)

            for j in range(n):
                newDpp[j] = max(lMax[j] - j, rMax[j] + j) + points[i][j]

            dpp = newDpp

        return max(dpp)
