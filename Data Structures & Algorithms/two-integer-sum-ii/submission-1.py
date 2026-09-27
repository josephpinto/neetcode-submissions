class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1

        while l < r:
            ssum = numbers[l] + numbers[r]
            if ssum == target:
                return [l+1,r+1]
            if ssum > target:
                r -= 1
            else:
                l += 1
                