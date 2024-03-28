class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        ml = 0

        cset = set() # Store unique chars only

        for r in range(len(s)):
            while s[r] in cset:
                cset.remove(s[l])
                l += 1

            cset.add(s[r])
            ml = max(ml, r - l + 1)
        return ml
