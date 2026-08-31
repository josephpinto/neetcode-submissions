class Solution:
    def rob(self, nums: List[int]) -> int:
        one,two = 0,0

        for n in nums:
            newVal = max(two+n, one)
            two = one
            one = newVal
        return one