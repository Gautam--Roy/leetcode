class Solution:
    def spiralOrder(self, matrix: [int]) -> [int]:
        res = []
        sr,sc,er,ec = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        while sr <= er and sc <= ec:       
            for c in range(sc , ec + 1):
                res.append(matrix[sr][c])
                # print(c)
            sr += 1
            
            for r in range(sr, er + 1):
                res.append(matrix[r][ec])
            ec -= 1
            
            if sr <= er and sc <= ec:
                for c in range(ec, sc - 1, -1):
                    res.append(matrix[er][c])
                er -= 1
                
                for r in range(er, sr - 1, -1):
                    res.append(matrix[r][sc])
                sc += 1
        return res
        


result = Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])