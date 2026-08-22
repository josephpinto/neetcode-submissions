class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i >=len(nums):
                return 0

            if i in memo:
                return memo[i]
            res = max(nums[i]+dfs(i+2),dfs(i+1))
            memo[i] = res
            return res
        dfs(0)
        return max(list(memo.values()))