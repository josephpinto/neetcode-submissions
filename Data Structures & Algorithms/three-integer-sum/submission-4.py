class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i,v in enumerate(nums):
            target = -v
            l,r = i+1, len(nums)-1
            if i>0 and v == nums[i-1]:
                continue
            while l<r:
                three = v + nums[l] + nums[r]
                if three > 0:
                    r -= 1
                elif three < 0:
                    l += 1
                else:
                    res.append([v, nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res
