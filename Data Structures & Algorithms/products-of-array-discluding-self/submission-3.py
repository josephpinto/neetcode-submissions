class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = []
        suffix_prod = []
        res = []

        prefix = 1
        for i,v in enumerate(nums):
            prefix_prod.append(prefix)
            prefix *= v
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            suffix_prod.append(suffix)
            suffix *= nums[i]
            suffix_prod[-1]*nums[i]
        suffix_prod = suffix_prod[::-1]

        for i in range(len(nums)):
            res.append(prefix_prod[i]*suffix_prod[i])
        return res