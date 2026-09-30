# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,valid_max, valid_min):
            if not node:
                return True
            if not valid_min < node.val < valid_max:
                return False
            valid_left = dfs(node.left,node.val, valid_min)
            valid_right = dfs(node.right, valid_max, node.val)
            return valid_left and valid_right

        return dfs(root, float('inf'), float('-inf'))