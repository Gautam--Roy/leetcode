class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ans = []
        # for i in range(len(nums)):
        #     temp = 1
        #     for j in range(len(nums)):
        #         if i == j: continue
        #         temp *= nums[j]
        #     ans.append(temp)
        # return ans

        left = [1] * len(nums)
        right = [1] * len(nums)
        ans = []

        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        print(left)
        print(right)

        for i in range(len(nums)):
            ans.append(left[i] * right[i])

        return ans
