class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, target):
            if i == len(nums):
                return 1 if target == 0 else 0
            if (i,target) in memo:
                return memo[(i,target)]
            res = 0
            res += dfs(i+1,target+nums[i])
            res += dfs(i+1,target-nums[i])
            memo[(i,target)] = res
            return res
        return dfs(0,target)