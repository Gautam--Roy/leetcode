class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:   
        ans = float('inf')
        minutes = [self.convertToMins(time) for time in timePoints]
        minutes.sort()

        for i in range(1, len(minutes)):
            ans = min(ans, minutes[i] - minutes[i-1])

        ans = min(ans, 1440 + minutes[0] - minutes[-1])

        return ans
    
    def convertToMins(self, time):
            h = int(time[:2])
            m = int(time[3:])
            return h * 60 + m
