class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict = {}
        for i,v in enumerate(nums):
            complement = target-v
            if complement in seen_dict:
                return [seen_dict[complement], i]
            seen_dict[v] = i
        