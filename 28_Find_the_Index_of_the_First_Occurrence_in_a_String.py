class Solution:
    def strStr(self, haystack: str, needle: str):
        if not needle:
            return 0
        needle_length = len(needle)

        for i in range(len(haystack) - needle_length + 1):
            if haystack[i : i + needle_length] == needle:
                return i
        return -1


result = Solution()
print(result.strStr("mississippi", "sippi"))  # needle present
print(result.strStr("mississippi", "soppi"))  # needle not present
print(result.strStr("mississippi", ""))  # no needle
