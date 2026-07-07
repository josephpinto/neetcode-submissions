class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []



        def dfs(curr_combo, cur_total, idx):
            if cur_total == target:
                res.append(curr_combo.copy())
                return
            if cur_total > target or idx > len(nums)-1:
                return
            
            curr_combo.append(nums[idx])
            dfs(curr_combo, cur_total + nums[idx], idx)
            curr_combo.pop()
            dfs(curr_combo, cur_total, idx+1)
        dfs([], 0, 0)
        return res