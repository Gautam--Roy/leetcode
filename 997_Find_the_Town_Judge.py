class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:

        count = {}
        for i in range(1, n + 1):
            count[i] = 0

        for i in trust:
            count[i[0]] = count.get(i[0]) - 1
            count[i[1]] = count.get(i[1]) + 1

        for i in range(1, n + 1):
            if count.get(i) == n - 1:
                return i

        return -1


# result = Solution().findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]])
result = Solution().findJudge(n=3, trust=[[1, 3], [2, 3]])
print(result)
