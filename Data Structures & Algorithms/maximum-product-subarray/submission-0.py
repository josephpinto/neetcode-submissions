class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        max_product = min_product = 1

        for n in nums:
            curr_with_max = max_product * n
            max_product = max(n*max_product, n, n*min_product)
            min_product = min(curr_with_max,n, n*min_product)
            res = max(res, max_product)
        return res