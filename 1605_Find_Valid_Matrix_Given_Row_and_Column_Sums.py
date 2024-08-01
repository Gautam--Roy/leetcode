class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        currentRow = 0
        currentCol = 0
        res = [[0 for _ in range(cols)] for _ in range(rows)]

        while currentRow < rows or currentCol < cols:
            if currentRow >= rows:
                res[rows - 1][currentCol] = colSum[currentCol]
                currentCol += 1
                continue
            elif currentCol >= cols:
                res[currentRow][cols - 1] = rowSum[currentRow]
                currentRow += 1
                continue

            value_to_put: int = min(rowSum[currentRow], colSum[currentCol])
            rowSum[currentRow] -= value_to_put
            colSum[currentCol] -= value_to_put
            res[currentRow][currentCol] = value_to_put

            if rowSum[currentRow] == 0:
                currentRow += 1
            if colSum[currentCol] == 0:
                currentCol += 1

        return res
