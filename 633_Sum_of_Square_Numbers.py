class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c <= 2:
            return True
        while c % 2 == 0:
            c /= 2
        if c % 4 == 3:
            return False
        sqrt_c = int(sqrt(c))
        for k in range(3, sqrt_c + 1, 4):
            exp = 0
            if c % k == 0:
                while c % k == 0:
                    exp += 1
                    c /= k
                if exp % 2 == 1:
                    return False
        return c % 4 != 3
