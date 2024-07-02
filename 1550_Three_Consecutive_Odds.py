class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        ans=0
        for x in arr:
            if x % 2 != 0:
                ans+=1
                if ans == 3:
                    return True
            else: ans = 0
        return False
