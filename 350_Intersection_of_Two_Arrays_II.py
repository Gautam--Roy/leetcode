class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        frq = {}
        ans = []
        for x in nums1:
            if x not in frq: frq[x] = 1
            else: frq[x] += 1
        for x in nums2:
            if x in frq and frq[x]>0:
                ans.append(x)
                frq[x] -= 1
        return ans
