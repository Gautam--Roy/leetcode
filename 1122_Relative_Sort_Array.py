class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        temp = 0
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j] == arr2[i]:
                    arr1[temp], arr1[j] = arr1[j], arr1[temp]
                    temp += 1
        arr1[temp:] = sorted(arr1[temp:])
        return arr1
