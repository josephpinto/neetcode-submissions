class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            product = 1
            newArray = nums[:i] + nums[i+1:]
            for j in newArray:
                product *= j
            result.append(product)
        return result