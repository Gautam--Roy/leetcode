class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frq = Counter(nums)
        heap = []
        for num in nums:
            heapq.heappush(heap, (frq[num], -num))
       
        result = []
        while heap:
            result.append(heapq.heappop(heap)[1] * -1)
       
        return result
