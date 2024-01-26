class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # Fastest solution on leet
        if moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R'):
            return True
        return False
        
result = Solution().judgeCircle("LL")
print(result)