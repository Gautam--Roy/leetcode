from collections import deque


class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        q = deque(sorted(tokens))
        score, max_score = 0,0
        
        while q:
            if power >= q[0]:
                t = q.popleft()
                power -= t
                score += 1
                max_score = max(score, max_score)
            elif score > 0:
                t = q.pop()
                power += t
                score-= 1
            else:
                break
        return max_score
    
    
    
result = Solution()
print(result.bagOfTokensScore([100, 200, 300, 400], 200))