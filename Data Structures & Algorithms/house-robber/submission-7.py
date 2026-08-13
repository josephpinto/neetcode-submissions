class Solution:
    def rob(self, nums: List[int]) -> int:
        one_back, two_back = 0,0
        for i in range(len(nums)-1,-1,-1):
            new = max(nums[i]+two_back, one_back)
            two_back, one_back = one_back, new
        return one_back

        
