from collections import Counter
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        candidates.sort()

        def dfs(i, cur_sum): 
            # Base cases
            if cur_sum == target:
                res.append(comb.copy())
                return
            if cur_sum > target or i == len(candidates):
                return
            
            # include candidate[i]
            comb.append(candidates[i])
            dfs(i+1, cur_sum + candidates[i])
            comb.pop()

            # do not include candidate[i]
            while (i+1 < len(candidates) and candidates[i] == candidates[i+1]):
                i += 1
            dfs(i+1, cur_sum)

        dfs(0, 0)
        return res