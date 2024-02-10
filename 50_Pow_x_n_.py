class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return 1 / (x * self.myPow(x, -n - 1))
        elif n % 2 == 0:
            result = self.myPow(x, n // 2)
            return result * result
        return x * self.myPow(x, n - 1)
        


result = Solution().myPow(2.10000, 2)
print(result)