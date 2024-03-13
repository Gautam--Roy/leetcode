class Solution:
    def pivotInteger(self, n: int) -> int:
        # n(a + l)/2

        def sum(s, e):
            nn = e - s + 1
            return nn * (s + e) / 2

        for i in range(1, n + 1):
            a = sum(1, i)
            b = sum(i, n)
            if a == b:
                return i
        return -1
