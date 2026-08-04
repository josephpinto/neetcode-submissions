class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        res = nums[0]
        while l<=r:
            mid = (l+r)//2

            # in left portion, go right
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                res = min(res, nums[mid])
                r = mid - 1
        return res
