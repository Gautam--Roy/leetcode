class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = Counter(words[0])
        for w in words:
            freq &= Counter(w)
        return list(freq.elements())
