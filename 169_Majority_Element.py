class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = 0
        max = None

        for n in nums:
            if temp == 0:
                max = n

            if n == max:
                temp += 1
            else:
                temp -= 1
        return max