class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        return len(s.split()[-1])


result = Solution().lengthOfLastWord("Hello World ")
print(result)
