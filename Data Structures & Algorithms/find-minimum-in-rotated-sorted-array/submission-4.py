class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1

        res = nums[0]
        while l<=r:
            if nums[l] <= nums[r]:
                res = min(res,nums[l])
                break
            midpoint = (l+r)//2
            cand = nums[midpoint]
            res = min(res, cand)
            if cand >= nums[l]:
                l = midpoint + 1
            else:
                r = midpoint - 1


        return res