class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        roots = set(dictionary)
        words = sentence.split()
        res = []

        for word in words:
            for i in range(len(word) + 1):
                prefix = word[:i]
                if prefix in roots:
                    res.append(prefix)
                    break
            else:
                res.append(word)

        return " ".join(res)
