class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob excluding first, rob excluding last. max of both
        if len(nums) == 1:
            return nums[0]
        return max(self.robSub(nums[1:]),self.robSub(nums[:-1]))
    def robSub(self, nums):
        r1,r2 = 0,0

        for n in nums:
            newVal = max(n+r1, r2)
            r1 = r2
            r2 = newVal
        return r2
        
