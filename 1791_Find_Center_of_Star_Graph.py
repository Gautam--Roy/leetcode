class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        a = {}
        for edge1, edge2 in edges:
            if edge1 not in a:
                a[edge1] = 0
            if edge2 not in a:
                a[edge2] = 0
            a[edge1] += 1
            a[edge2] += 1
        return max(a, key=a.get)
