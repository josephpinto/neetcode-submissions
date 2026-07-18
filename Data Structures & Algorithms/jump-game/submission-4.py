class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False]*len(nums)
        dp[0] = True
        for i,max_jump in enumerate(nums):
            if dp[i] == False or nums[i] == 0:
                continue
            
            for jump in range(max_jump):
                if i+jump+1 < len(nums):
                    dp[i+jump+1] = True
        return dp[-1] == True