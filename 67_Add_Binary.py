class Solution:
    def addBinary(self, a: str, b: str) -> str:
        A = int(a,2)
        B = int(b,2)
        return bin(A + B)[2:] # padding the 0b notation in front of the binary result

result1 = Solution().addBinary("11","1")
print(result1)