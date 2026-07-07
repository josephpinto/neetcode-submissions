class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        
        def dfs(curr_perm, cands_remaining):
            if not cands_remaining:
                res.append(curr_perm.copy())
                return
            for c in set(cands_remaining):
                curr_perm.append(c)
                cands_remaining.remove(c)
                dfs(curr_perm, cands_remaining)
                curr_perm.pop()
                cands_remaining.add(c)
        dfs([], set(nums))
        return res

            