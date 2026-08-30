class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        candidates.sort()
        def dfs(i, target):
            if target == 0:
                res.append(curr[:])
                return
            if target < 0 or i == len(candidates):
                return
            curr.append(candidates[i])
            dfs(i+1,target-candidates[i])
            curr.pop()
            new_idx = i+1
            curr_num = candidates[i]
            while new_idx < len(candidates) and candidates[new_idx] == candidates[new_idx-1]:
                new_idx += 1
            dfs(new_idx,target)
            
        dfs(0,target)
        return res  