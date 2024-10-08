class Solution:
    def minSwaps(self, s: str) -> int:
        res = 0
        for brac in s:
            if brac == '[':
                res += 1
            elif res > 0:
                res -= 1
        return (res + 1) // 2
