class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l = len(heights)
        p = {}
        for i in range(l):
            p[heights[i]] = names[i]
        
        
        heights.sort(reverse=True)

        for i in range(l):
            names[i] = p[heights[i]]
        return names
