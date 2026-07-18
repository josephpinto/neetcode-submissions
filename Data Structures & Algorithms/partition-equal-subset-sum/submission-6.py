class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2: 
            return False
        
        cache = {}
        def dfs(i, target):
            if (i,target) in cache:
                return cache[(i,target)]
            if target == 0:
                cache[(i,target)] = True
                return True
            if i >= len(nums) or target < 0:
                cache[(i,target)] = False
                return False
            res = dfs(i+1,target) or dfs(i+1,target-nums[i])
            cache[(i,target)] = res
            return res
        return dfs(0,sum(nums)/2)



