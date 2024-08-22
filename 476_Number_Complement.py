class Solution:
        def findComplement(self, num: int) -> int:
            bitLen = num.bit_length()
        temp = (1 << bitLen) - 1
        return num ^ temp
