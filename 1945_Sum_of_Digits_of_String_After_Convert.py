class Solution(object):
    def getLucky(self, s, k):
        num = ''
        for i in s:
            num += str(ord(i) - ord('a') + 1)
        while k > 0:
            temp = 0
            for i in num:
                temp += int(i)
            num = str(temp)
            k -= 1
        return int(num)
