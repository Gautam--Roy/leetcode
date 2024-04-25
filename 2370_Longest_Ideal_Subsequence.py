class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        alphas = [0] * 26

        for c in s:
            cur = ord(c) - ord("a")

            mx = max(alphas[max(0, cur - k) : min(26, cur + k + 1)])

            alphas[cur] = 1 + mx
        return max(alphas)
