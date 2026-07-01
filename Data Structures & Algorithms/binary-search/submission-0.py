class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l<=r:
            mid = (l+r)//2
            candidate = nums[mid]
            if candidate == target:
                return mid
            if candidate > target:
                r = mid-1
            else:
                l = mid+1
        return -1