class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <=2:
            return max(nums)
        first = nums[0]
        second = max(first,nums[1])


        for i in range(2, len(nums)):
            num = nums[i]
            curr_sum = max(second, first+num)
            first,second = second, curr_sum
        return second