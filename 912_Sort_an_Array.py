class Solution:
    def sortArray(self, nums):
        self.ms(nums, 0, len(nums))
        return nums

    def ms(self, arr, s, e):
        if e - s <= 1:
            return

        m = s + (e - s) // 2

        self.ms(arr, s, m)
        self.ms(arr, m, e)

        self.merge(arr, s, m, e)

    def merge(self, arr, s, m, e):
        i, j, k = s, m, 0
        mix = [0] * (e - s)

        while i < m and j < e:
            if arr[i] < arr[j]:
                mix[k] = arr[i]
                i += 1
            else:
                mix[k] = arr[j]
                j += 1
            k += 1

        while i < m:
            mix[k] = arr[i]
            i += 1
            k += 1
        while j < e:
            mix[k] = arr[j]
            j += 1
            k += 1

        for l in range(len(mix)):
            arr[s + l] = mix[l]
