class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        tempProd = [0] * (len(num1) + len(num2))
        for m2 in range(len(num2) - 1, -1, -1):
            carry = 0
            for m1 in range(len(num1) - 1, -1, -1):
                prod = int(num1[m1]) * int(num2[m2]) + carry
                ones = prod % 10
                carry = prod // 10
                tempProd[m1 + m2 + 1] += ones
                carry += tempProd[m1 + m2 + 1] // 10
                tempProd[m1 + m2 + 1] %= 10
            tempProd[m2] += carry

        result = ''.join(map(str, tempProd)).lstrip('0')
        return '0' if not result else result

result = Solution().multiply("123", "456")
print(result)
