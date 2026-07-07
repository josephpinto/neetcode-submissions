class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(idx, subset):
            if idx >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[idx])
            dfs(idx+1, subset)
            subset.pop()
            original_num = nums[idx]
            while idx < len(nums) and nums[idx] == original_num:
                idx += 1
            dfs(idx,subset)
        dfs(0, [])
        return res

