class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        char = ""
        resultArray = []
        for c in digits:
            char += str(c)

        char = int(char) + 1
        for c in str(char):
            resultArray.append(int(c))
        return resultArray


result = Solution().plusOne([9])
print(result)
