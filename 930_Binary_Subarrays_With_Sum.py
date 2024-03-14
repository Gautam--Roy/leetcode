class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum_count = {0: 1}
        count = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            if prefix_sum - goal in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - goal]
            prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1

        return count
