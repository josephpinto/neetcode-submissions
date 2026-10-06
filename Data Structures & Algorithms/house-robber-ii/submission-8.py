class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.robSubset(nums[1:]), self.robSubset(nums[:-1]))
    def robSubset(self,nums):
        one,two = 0,0

        for n in nums:
            newVal = max(n+two,one)
            two = one
            one = newVal
        return one