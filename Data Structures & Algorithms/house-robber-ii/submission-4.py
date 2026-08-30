class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob excluding first, rob excluding last. max of both
        if len(nums) == 1:
            return nums[0]
        return max(self.robSub(nums[1:]),self.robSub(nums[:-1]))
    def robSub(self, nums):

    
        memo = {}

        def dfs(i):
            if i >= len(nums):
                return 0
            if i in memo: return memo[i]
            res =  max(nums[i]+dfs(i+2), dfs(i+1))
            memo[i] = res
            return res
        
        return dfs(0)
            
        
