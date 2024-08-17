class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        sm = arrays[0][0]
        lg = arrays[0][-1]
        mx = 0

        for i in range(1, len(arrays)):
            arr = arrays[i]
            mx = max(mx, abs(arr[-1] - sm), abs(lg - arr[0]))
            sm = min(sm, arr[0])
            lg = max(lg, arr[-1])
        return mx
