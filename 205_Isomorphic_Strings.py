class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lookup = {}
        lookup2 = {}
        a, b = [], []
        i = 1
        for w in s:
            if w not in lookup:
                lookup[w] = i
                i += 1
            a.append(lookup[w])

        j = 1
        for ws in t:
            if ws not in lookup2:
                lookup2[ws] = j
                j += 1
            b.append(lookup2[ws])

        return a == b
