class Solution:
    def combinationSum2(self, cand, target):
        cand.sort()
        result = []
        state = []
        self.dfs(cand, 0, target, state, result)
        return result
    
    def dfs(self, cand, cur, target, state, result):
        if target == 0:
            result.append(state.copy())
            return
        if target < 0:
            return
        
        for i in range(cur, len(cand)):
            if i > cur and cand[i] == cand[i - 1]:
                continue
            state.append(cand[i])
            self.dfs(cand, i + 1, target - cand[i], state, result)
            state.pop()
