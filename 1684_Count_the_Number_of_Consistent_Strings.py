class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        def checkConsistent(needle, hay):
            con = 0
            for i in needle:
                if i not in hay:
                    return False
            return True

        for i in words:
            if checkConsistent(i, allowed):
                ans += 1

        return ans    

            

