class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search to find min in log(n)
        l,r = 0, len(nums)-1
        result = nums[0]
        while l<=r:
            if(nums[l] <= nums[r]):
                result = min(result, nums[l])
                break
            mid = (l+r)//2
            result = min(result,nums[mid])
            # [3,4,5,6,7,1,2,3]
            if nums[mid] >= nums[l]:
                l = mid+1
            else:
                r = mid-1
        return result

            