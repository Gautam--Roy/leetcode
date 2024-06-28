class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        arr = [0] * n
        for a,b in roads:
            arr[a] += 1 
            arr[b] += 1
        arr.sort() 
        sum = 0
        for i in range(len(arr)):
            sum += arr[i] * (i+1)  
        
        return sum
