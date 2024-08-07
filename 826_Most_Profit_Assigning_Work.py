class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        mp = 0
        best = 0
        i = 0
        n = len(jobs)
        for ability in worker:
            while i < n and jobs[i][0] <= ability:
                best = max(best, jobs[i][1])
                i += 1
            mp += best

        return mp
