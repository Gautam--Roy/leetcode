class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars = set()
        ans = 0
        for char in s:
            if char in chars:
                chars.remove(char)
                ans += 2
            else:
                chars.add(char)
        if chars:
            ans += 1
        return ans
