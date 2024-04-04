class Solution:
    def maxDepth(self, s: str) -> int:
        a = 0
        ans = 0

        for c in s:
            if c == "(":
                a += 1
                ans = max(a, ans)
            if c == ")":
                a -= 1
        return ans
