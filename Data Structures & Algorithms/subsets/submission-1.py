class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            new_subsets = []
            for subset in res:
                new_subsets.append([n]+subset)
            res += new_subsets
        return res
        


