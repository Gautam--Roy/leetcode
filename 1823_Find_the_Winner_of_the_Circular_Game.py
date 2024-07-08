class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        fs=[]
        pos = 0
        for f in range(n):
            fs.append(f+1)
        while n > 1:
            pos = (pos + (k-1)) % n
            fs.pop(pos)
            n -= 1

        return fs[0]
