class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cands, curr):
            if not cands:
                res.append(curr)
                return
            for n in cands.copy():
                cands.remove(n)
                dfs(cands,curr+[n])
                cands.add(n)
        dfs(set(nums),[])
        return res