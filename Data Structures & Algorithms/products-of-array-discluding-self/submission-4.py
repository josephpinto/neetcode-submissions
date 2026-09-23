class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pres = [1]
        suffs = [1]
        for i in range(1,len(nums)):
            pres.append(pres[i-1]*nums[i-1])
        for i in range(len(nums)-2,-1,-1):
            suffs.append(suffs[-1]*nums[i+1])
        suffs = suffs[::-1]
        res = []
        for i in range(len(nums)):
            res.append(pres[i]*suffs[i])
        return res