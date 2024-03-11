class Solution:
    def customSortString(self, order: str, s: str) -> str:

        result = []
        for i in order:
            if i in s:
                n = s.count(i)
                result.append(i * n)
                s = s.replace(i, "")
        return "".join(result) + s
