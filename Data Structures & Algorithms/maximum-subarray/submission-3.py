class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        global_max = nums[0]
        for n in nums[1:]:
            if curr_sum < 0:
                curr_sum = n
            else:
                curr_sum += n
            global_max = max(global_max,curr_sum)
        return global_max