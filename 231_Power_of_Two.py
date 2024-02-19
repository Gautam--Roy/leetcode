class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True

        while n % 2 == 0:
            if n == 2:
                return True
            else:
                n = n / 2
        return False

        # # 16
        # # 16 / 2 = 8 rem 0
        # 8 / 2 = 4 rem 0
        # 4 / 2 = 2 rem 0
        # 2 / 2 = 1 rem 0
