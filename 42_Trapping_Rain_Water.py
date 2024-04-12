class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)

        def get_prefix_max(h):
            pref = [0]
            for i in range(N):
                pref.append(max(h[i], pref[-1]))
            return pref

        left = get_prefix_max(height)
        right = get_prefix_max(height[::-1])[::-1]

        water = 0
        for i in range(N):
            water += max(min(left[i], right[i + 1]) - height[i], 0)

        return water
