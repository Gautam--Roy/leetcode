class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        n = len(grid)
        distToThief = self._getDistToThief(grid, n)

        def hasValidPath(safeness: int) -> bool:
            if distToThief[0][0] < safeness:
                return False

            q = collections.deque([(0, 0)])
            seen = {(0, 0)}

            while q:
                i, j = q.popleft()
                if distToThief[i][j] < safeness:
                    continue
                if i == n - 1 and j == n - 1:
                    return True
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < n and (x, y) not in seen:
                        q.append((x, y))
                        seen.add((x, y))

            return False

        return (
            bisect.bisect_left(range(n * 2), True, key=lambda m: not hasValidPath(m))
            - 1
        )

    def _getDistToThief(self, grid: List[List[int]], n: int) -> List[List[int]]:
        distToThief = [[0] * n for _ in range(n)]
        q = collections.deque()
        seen = set()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    seen.add((i, j))

        dist = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                distToThief[i][j] = dist
                for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < n and (x, y) not in seen:
                        q.append((x, y))
                        seen.add((x, y))
            dist += 1

        return distToThief
