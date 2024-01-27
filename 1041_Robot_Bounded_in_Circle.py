class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dir = [[0, 1],[1, 0],[0, -1],[-1, 0]]
        init = [0,0]
        cd = 0
        for m in instructions:                    
            if m == "L":
                cd += -1
            if m == "R":
                cd += 1
            if m == "G":
                init[0] += dir[cd][0]
                init[1] += dir[cd][1]
        return init == [0,0] or cd%4 != 0