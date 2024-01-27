class Solution:
    def tictactoe(self, moves: [[int]]) -> str:
        a,b = [0]*8,[0]*8
        
        for i,move in enumerate(moves):
            row,col = moves[i]
            if i% 2==0:
                player = a
            else:
                player = b
                
            player[row] += 1
            player[col +3 ] += 1
            
            if row == col:
                player[6] += 1
            if row == 2 - col:
                player[7] += 1
                
        for i, _ in enumerate(a):
            if a[i] == 3:
                return "A"
            elif b[i] == 3:
                return "B"
            
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"

result = Solution().tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]])
print(result)