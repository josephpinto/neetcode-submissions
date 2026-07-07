class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []


        def dfs(curr_subset,idx):
            if idx > len(nums)-1:
                res.append(curr_subset.copy())
                return
            curr_subset.append(nums[idx])
            dfs(curr_subset, idx+1)
            curr_subset.pop()
            dfs(curr_subset, idx+1)
            

        dfs([],0)

        return res



