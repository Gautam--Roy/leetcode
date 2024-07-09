class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        aa = 0
        tw = 0
        for a, t in customers:
            aa = max(aa, a) + t
            tw += aa - a
        
        return tw / len(customers)
