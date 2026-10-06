class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        prod = 1
        for r,v in enumerate(nums):
            prod*=v
            while l <= r and prod >= k:
                prod /= nums[l]
                l+= 1
            if prod<k:
                res += (r-l+1)
        return res
