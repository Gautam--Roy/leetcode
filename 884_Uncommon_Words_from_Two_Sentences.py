class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        strings = s1.split(' ')
        strings += (s2.split(' '))
        cnt = Counter(strings)

        temp = []
        for s, c in cnt.items():
            if c == 1:
                temp.append(s)
        return temp
