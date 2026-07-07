class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(idx, curr_set):
            if idx >= len(nums):
                res.append(curr_set)
                return
            dfs(idx+1, curr_set)
            dfs(idx+1, curr_set+[nums[idx]])


        dfs(0, [])
        return res


