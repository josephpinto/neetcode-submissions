class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = nums[0]
        max_product = min_product = 1
        for n in nums:
            temp_max = n*max_product
            max_product = max(n,n*max_product,n*min_product)
            min_product = min(n,temp_max,n*min_product)
            global_max = max(global_max,max_product)
        return global_max
