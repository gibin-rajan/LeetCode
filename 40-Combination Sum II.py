class Solution:
    def comb(self, i, sub, ans, candidates, t):
        if t == 0:
            ans.append(list(sub))
            return
        if i == len(candidates) or t < candidates[i]:
            return
        for ind in range(i, len(candidates)):
            if ind > i and candidates[ind - 1] == candidates[ind]:
                continue
            sub.append(candidates[ind])
            self.comb(ind + 1, sub, ans, candidates, t - candidates[ind])
            sub.pop()
    
    def combinationSum2(self, candidates, target):
        ans = []
        sub = []
        candidates.sort()
        self.comb(0, sub, ans, candidates, target)
        return ans