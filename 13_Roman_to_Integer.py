class Solution:
    def romanToInt(self, s: str) -> int:
        rmap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        tot = 0
        slen = len(s)
        for i in range(slen):
            if i < slen - 1 and rmap[s[i]] < rmap[s[i + 1]]:
                tot -= rmap[s[i]]
            else:
                tot += rmap[s[i]]
        return tot


result = Solution().romanToInt("III")
print(result)
