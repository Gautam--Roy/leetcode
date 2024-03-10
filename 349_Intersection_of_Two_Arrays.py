class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = set(nums1)
        r = []

        for i in nums2:
            if i in c:
                r.append(i)
                c.remove(i)
        return r

        # Other solutions :
        # return list(set(nums1) & set(nums2))
        # return list(set(nums1).intersection(set(nums2)))
