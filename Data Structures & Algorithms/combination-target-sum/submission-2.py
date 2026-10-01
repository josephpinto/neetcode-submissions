class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(curr,i):
            if sum(curr) == target:
                res.append(curr)
                return
            if sum(curr) > target or i == len(nums):
                return
            dfs(curr+[nums[i]],i)
            dfs(curr,i+1)
        dfs([],0)
        return res
