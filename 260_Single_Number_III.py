class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dd = defaultdict(int)
        for n in nums:
            dd[n] += 1

        ans = []
        for num, f in dd.items():
            if f == 1:
                ans.append(num)
        return ans
