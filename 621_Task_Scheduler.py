class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord("A")] += 1
        freq.sort()
        print(freq)
        chunk = freq[25] - 1
        print(chunk)
        idle = chunk * n
        print(idle)

        for i in range(24, -1, -1):
            idle -= min(chunk, freq[i])
            print("---")
            print(idle)

        return len(tasks) + idle if idle >= 0 else len(tasks)
