
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i,j = len(spaces), len(s)
        temp = [" "] * (i+j)
        x = 0
        for m,n in enumerate(s):
            if x < i and m == spaces[x]:
                x+=1
            temp[m + x] = s[m]
        return "".join(temp)
