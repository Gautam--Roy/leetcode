class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        n = len(heights)

        ans = 0

        for i in range(n):
            if heights[i] != expected[i]:
                ans += 1

        return ans
