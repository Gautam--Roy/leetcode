class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        lc = ""
        for c in s:
            if 65 <= ord(c) <= 90:
                lc += (chr(ord(c) + 32))
            else:
                lc += c
        return lc
    
result = Solution().toLowerCase("Hel&#^lo")
print(result)