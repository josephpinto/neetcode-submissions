class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(idx, curr_sum):
            if idx == len(nums):
                return 1 if curr_sum == target else 0
            if (idx,curr_sum) in cache: return cache[(idx,curr_sum)]
            add_sum = curr_sum + nums[idx]
            sub_sum = curr_sum - nums[idx]
            
            res1 = dfs(idx+1,add_sum)
            res2 = dfs(idx+1,sub_sum)
            cache[(idx,curr_sum)] = res1+res2
            return res1+res2
        return dfs(0,0)
