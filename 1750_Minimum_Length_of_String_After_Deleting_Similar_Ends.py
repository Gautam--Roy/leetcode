class Solution:
    def minimumLength(self, s: str) -> int:
        q = deque(s)

        while len(q) > 1 and q[0] == q[-1]:
            c = q[0]
            while len(q) > 0 and c == q[0]:
                q.popleft()
            while len(q) > 0 and c == q[-1]:
                q.pop()
        return len(q)
