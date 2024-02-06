class Solution:
    def checkStraightLine(self, coordinates: [int]) -> bool:
        if len(coordinates) == 2:
            return True
        for i in range(0, len(coordinates) - 2):
            # if (coordinates[i+1][1] - coordinates[i][1]) / (coordinates[i+1][0] - coordinates[i][0]) != (coordinates[i+2][1] - coordinates[i+1][1]) / (coordinates[i+2][0] - coordinates[i+1][0]):
            if (coordinates[i+1][1] - coordinates[i][1]) * (coordinates[i+2][0] - coordinates[i+1][0]) != (coordinates[i+2][1] - coordinates[i+1][1]) * (coordinates[i+1][0] - coordinates[i][0]):
                return False
        return True 
    
result = Solution().checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])
# result = Solution().checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])
print(result)