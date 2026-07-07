class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()

        def dfs(i, curr_sum, curr_combo):
            if curr_sum == target:
                res.append(curr_combo.copy())
                return
            if curr_sum > target or i > len(candidates) -1:
                return
            # include
            num = candidates[i]
            curr_combo.append(num)
            dfs(i+1, curr_sum+num, curr_combo)
            # exclude, skip dupes
            curr_combo.pop()
            while i < len(candidates) and candidates[i] == num:
                i+= 1
            dfs(i, curr_sum, curr_combo)
        dfs(0,0,[])
        return res