class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cl = 2 * n - 2
        tc = time % cl
        if tc < n:
            return 1 + tc
        else:
            return cl + 1 - tc

