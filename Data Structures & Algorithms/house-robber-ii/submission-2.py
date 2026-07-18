class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.robHouse(nums[1:]), self.robHouse(nums[:-1]))

    
    def robHouse(self, nums):
        first = second = 0
        for n in nums:
            new = max(n+first,second)
            first,second = second, new
        return second