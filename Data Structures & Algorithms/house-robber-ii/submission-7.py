class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.robNums(nums[:-1]),self.robNums(nums[1:]))


    def robNums(self,nums):
        one,two = 0,0

        for i in range(len(nums)):
            curr = max(two+nums[i],one)
            two = one
            one = curr
        return one