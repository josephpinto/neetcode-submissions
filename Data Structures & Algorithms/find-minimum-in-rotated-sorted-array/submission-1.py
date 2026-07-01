class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if nums[0] <= nums[-1]:
            return nums[0]
        # binary search to find min in log(n)
        l,r = 0, len(nums)-1

        while l<=r:
            mid = (l+r)//2
            # if nums[mid+1] < nums[mid]:
            #     return nums[mid+1]
            
            # [3,4,5,6,1,2]
            if mid != 0 and nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] < nums[0]:
                r = mid - 1
            else:
                l = mid + 1
        return l

            