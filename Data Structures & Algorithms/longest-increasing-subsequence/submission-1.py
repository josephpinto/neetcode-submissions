class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # LIS starting at index i
        DP = [1]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            curr_max = 1
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    curr_max = max(curr_max,1+DP[j])
            DP[i] = curr_max
        return max(DP)



        