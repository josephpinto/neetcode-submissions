# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max = float('-inf')
        def dfs(node):
            nonlocal global_max
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            curr_max = max(left+node.val,right+node.val,node.val)
            global_max = max(global_max,curr_max,left+right+node.val)
            return curr_max
        dfs(root)
        return global_max