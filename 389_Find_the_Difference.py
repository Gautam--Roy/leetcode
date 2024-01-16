class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_of_s = {}
        count_of_t = {}

        for char in s:
            count_of_s[char] = count_of_s.get(char, 0) + 1
        for char in t:
            count_of_t[char] = count_of_t.get(char, 0) + 1

        for char in count_of_t:
            if char not in count_of_s or count_of_t[char] > count_of_s[char]:
                return char


result = Solution().findTheDifference("abc", "abce")
print(result)
