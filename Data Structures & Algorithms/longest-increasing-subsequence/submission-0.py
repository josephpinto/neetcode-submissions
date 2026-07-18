class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        DP = [1]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            max_curr = 1
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    max_curr = max(max_curr,1+DP[j])
                DP[i] = max_curr
        return max(DP)

