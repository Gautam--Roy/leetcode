class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for p in words:
            if p == p[::-1]:
                return p
        return ""
