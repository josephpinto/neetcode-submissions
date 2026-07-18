class Solution:
    def rob(self, nums: List[int]) -> int:
        first,second = 0,0


        for house_val in nums:
            new = max(house_val+first,second)
            first,second = second, new
        return second