# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def maxSumDfs(node):
            nonlocal max_sum
            if not node:
                return 0 
            max_sum_left, max_sum_right = maxSumDfs(node.left) , maxSumDfs(node.right)

            max_with_both = max_sum_left + max_sum_right + node.val
            curr_max = max(node.val+max_sum_right, node.val+max_sum_left, node.val)
            max_sum = max(curr_max, max_sum, max_with_both)
            return curr_max


        maxSumDfs(root)

        return max_sum




