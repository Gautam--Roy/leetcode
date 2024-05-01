class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = word.find(ch)
        ans = ""
        for i in range(n, -1, -1):
            ans += word[i]

        ans += word[n + 1 :]
        return ans
