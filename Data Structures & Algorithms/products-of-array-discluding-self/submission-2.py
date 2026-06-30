class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        # nums = [1,2,4,6]
        # prodBefore = [1,1,2,8]
        # prodAfter = [48,24,6,1]

        prodBefore = []
        prodAfter = []
        
        # befores
        prefix = 1
        for i,n in enumerate(nums):
            prodBefore.append(prefix)
            prefix *=n
        print('befores',prodBefore)

        # afters
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            prodAfter.append(suffix)
            suffix*=nums[i]
        prodAfter.reverse()
        for i in range(len(nums)):
            result.append(prodBefore[i]*prodAfter[i])
        return result


