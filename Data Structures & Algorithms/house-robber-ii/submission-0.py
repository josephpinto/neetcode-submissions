class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(nums):
            first = second = 0
            for n in nums:
                curr = max(first+n,second)
                first,second = second,curr
            return second
        return max(helper(nums[1:]), helper(nums[:-1]))