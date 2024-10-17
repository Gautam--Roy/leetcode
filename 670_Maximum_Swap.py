class Solution:
    def maximumSwap(self, num: int) -> int:
        n = list(str(num))
        last = {int(d): i for i,d in enumerate(n)}
        for i, digit in enumerate(n):
            for d in range(9, int(digit), -1):
                if last.get(d, -1) > i:
                    n[i], n[last[d]] = n[last[d]], n[i]
                    return int(''.join(n))
        return num
