class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = sorted(score, reverse=True)
        ranks = {}

        for i in range(len(score)):
            if i == 0:
                ranks[temp[i]] = "Gold Medal"
            elif i == 1:
                ranks[temp[i]] = "Silver Medal"
            elif i == 2:
                ranks[temp[i]] = "Bronze Medal"
            else:
                ranks[temp[i]] = str(i + 1)

        ans = []
        for i in score:
            ans.append(ranks[i])
        return ans
