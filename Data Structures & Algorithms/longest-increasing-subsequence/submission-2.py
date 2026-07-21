class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1]*(len(nums))

        for start in range(len(nums)-1,-1,-1):
            for cand in range(start+1,len(nums)):
                if nums[cand] > nums[start]:
                    LIS[start] = max(LIS[start], 1+LIS[cand])
        return max(LIS)