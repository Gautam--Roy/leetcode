class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        ans = []
        for i in range(len(operations)):
            if operations[i] == "+":
                ans.append(ans[-1] + ans[-2])
            elif operations[i] == "D":
                ans.append(ans[-1] * 2)
            elif operations[i] == "C":
                ans.pop()
            else:
                ans.append(int(operations[i]))
        return sum(ans)
result = Solution().calPoints(["5","-2","4","C","D","9","+","+"])
print(result)