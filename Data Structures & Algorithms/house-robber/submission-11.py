class Solution:
    def rob(self, nums: List[int]) -> int:
        one,two = 0,0

        for n in nums:
            new_max = max(two+n,one)
            two = one
            one = new_max
        return one