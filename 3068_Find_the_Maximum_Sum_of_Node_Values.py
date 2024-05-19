class Solution:
    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        n: int = len(nums)
        temp: list[list[int]] = [[-1 for _ in range(2)] for _ in range(n)]

        def calculate_max(cur_ind, is_even) -> int:
            if cur_ind == n:
                return 0 if is_even else -float("inf")
            if temp[cur_ind][is_even] != -1:
                return temp[cur_ind][is_even]
            no_xor = nums[cur_ind] + calculate_max(cur_ind + 1, is_even)
            with_xor = (nums[cur_ind] ^ k) + calculate_max(cur_ind + 1, not is_even)

            mx_possible = max(no_xor, with_xor)
            temp[cur_ind][is_even] = mx_possible
            return mx_possible

        return calculate_max(0, 1)
