class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # n = 0
        # for i in range(n, len(nums)):
        #     for j in range(n+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        hash = {}

        for i in range(len(nums)):
            hash[nums[i]] = i

        for i in range(len(nums)):
            y = target - nums[i]
            if y in hash and hash[y] != i:
                return [i, hash[y]]
