class Solution:
    def makeGood(self, s: str) -> str:
        chars = []
        for c in s:
            if chars and abs(ord(c) - ord(chars[-1])) == 32:
                chars.pop()
            else:
                chars.append(c)

        return "".join(chars)
