class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        lenAr = len(arr)

        @cache
        def dep(i):
            if i == lenAr:
                return 0
            res = 0
            current_max = 0
            for j in range(i, min(lenAr, i + k)):
                current_max = max(arr[j], current_max)
                res = max(res, current_max * (j - i + 1) + dep(j + 1))
            return res

        return dep(0)
