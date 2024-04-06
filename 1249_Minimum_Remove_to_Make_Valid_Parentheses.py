class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open = 0
        temp = []
        ans = []
        for c in s:
            if c == "(":
                open += 1
                temp.append(c)
            elif c == ")" and open > 0:
                open -= 1
                temp.append(c)
            elif c != ")":
                temp.append(c)

        for c in temp[::-1]:
            if c == "(" and open > 0:
                open -= 1
            else:
                ans.append(c)

        return "".join(ans[::-1])
