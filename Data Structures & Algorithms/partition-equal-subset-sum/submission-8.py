class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if not summ % 2 == 0:
            return False
        target = summ // 2
        memo = {}
        def dfs(i, target):
            if target == 0:
                return True
            if target < 0 or i >= len(nums):
                return False
            if (i,target) in memo:
                return memo[(i,target)]
            
            memo[(i,target)] = dfs(i+1, target-nums[i]) or dfs(i+1, target)
            return memo[(i,target)]


        return dfs(0,target)