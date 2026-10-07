class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summ = 0
        for i in range(len(nums)+1):
            summ += i
        actual_sum = 0
        for n in nums:
            actual_sum += n
        return summ - actual_sum