class Solution:
    def isHappy(self, n: int) -> bool:
        
        nums = set()
        while True:
            string = str(n)
            curr_sum = 0
            for digit in string:
                curr_sum += int(digit)*int(digit)
            if curr_sum in nums: return False
            if curr_sum == 1: return True
            nums.add(curr_sum)
            n = curr_sum