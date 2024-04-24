class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0] * 38
        t[0], t[1], t[2] = 0, 1, 1
        for i in range(0, 35):
            t[i + 3] = t[i] + t[i + 1] + t[i + 2]

        return t[n]
