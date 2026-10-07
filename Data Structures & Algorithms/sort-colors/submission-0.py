class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r = 0, len(nums)-1
        i = 0

        while i <= r:
            tmp = nums[i]
            if tmp == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif tmp == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            else:
                # just found a 1, move on
                i += 1
