class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        # nums = [1,2,4,6]
        # prodBefore = [1,1,2,8]
        # prodAfter = [48,24,6,1]

        prodBefore = []
        prodAfter = []
        
        # befores
        for i,n in enumerate(nums[:-1]):
            if i == 0:
                prodBefore.append(1)
            prodBefore.append(prodBefore[-1]*n)
        print('befores',prodBefore)

        # afters
        for i,n in enumerate(nums[::-1][:-1]):
            if i == 0:
                prodAfter.append(1)
            prodAfter.append(prodAfter[-1]*n)
        prodAfter.reverse()
        print('afters',prodAfter)
        for i in range(len(nums)):
            result.append(prodBefore[i]*prodAfter[i])
        return result


