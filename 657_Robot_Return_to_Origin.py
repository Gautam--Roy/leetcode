class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        R = [0, 1]
        L=  [0 , -1]
        U = [1, 0]
        D = [-1, 0]
        P = [0,0]
        for m in range(len(moves)):
            match moves[m]:
                case "R":
                    P[1] += R[1]
                case "L":
                    P[1] += L[1]
                case "U":
                    P[0] += U[0]
                case "D":
                    P[0] += D[0]
                case _:
                    pass
        if P == [0,0]:
            return True
        else: return False
        
        
result = Solution().judgeCircle("LL")
print(result)