class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = 1
        res = nums[0]
        for n in nums:
            tmp_max_prod = max_prod
            newVal = max_prod*n
            res = max(res, n,max_prod*n, min_prod*n)
            max_prod = max(n*max_prod, n, n*min_prod)
            min_prod = min(n, n*tmp_max_prod, n*min_prod)
        return res
