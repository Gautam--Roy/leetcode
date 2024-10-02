class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {}
        sorts = sorted(list(set(arr)))
        

        for index in range(len(sorts)): 
            ranks[sorts[index]] = index + 1
          

        for index in range(len(arr)): 
            arr[index] = ranks[arr[index]]
        
        return arr
