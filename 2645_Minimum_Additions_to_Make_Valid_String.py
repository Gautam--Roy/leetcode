class Solution:
    def addMinimum(self, word: str) -> int:
        abcCount = 0
        n = len(word)
        i = 0
        while i < n:
            if word[i:i+3] == "abc":
                abcCount += 0
                i += 3
            elif word[i:i+2] == "ab" or word[i:i+2] == "bc" or word[i:i+2] == "ac":
                abcCount += 1
                i += 2
            else: 
                abcCount += 2
                i += 1
        return abcCount
