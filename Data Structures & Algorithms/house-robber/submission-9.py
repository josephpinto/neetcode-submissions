class Solution:
    def rob(self, nums: List[int]) -> int:
        
        one, two = 0,0

        for i in range(len(nums)):
            curr = max(two+nums[i],one)
            two = one
            one = curr
        return one