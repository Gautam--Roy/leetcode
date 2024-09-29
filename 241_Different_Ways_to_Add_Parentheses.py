class Solution:
        def diffWaysToCompute(self, inputStr: str) -> List[int]:
            def calc(left, right, operator):
                if operator == '+':
                    return left + right
            elif operator == '-':
                    return left - right
            elif operator == '*':
                    return left * right
        def diffWaysToComputeHelper(inputStr):
                if inputStr.isdigit():
                        return [int(inputStr)]
            outputList = []
                for i in range(len(inputStr)):
                        if inputStr[i] in ['+', '-', '*']:
                            leftResults = diffWaysToComputeHelper(inputStr[:i])
                            rightResults = diffWaysToComputeHelper(inputStr[i+1:])
                            for left in leftResults:
                                    for right in rightResults:
                                            outputList.append(calc(left, right, inputStr[i]))
                            return outputList
        return diffWaysToComputeHelper(inputStr)


        # Study later:
