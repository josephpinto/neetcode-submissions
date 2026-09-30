# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(node):
            nonlocal res
            if not res:
                return False
            if not node:
                return 0
            left,right = dfs(node.left), dfs(node.right)
            if abs(left-right) > 1:
                res = False
                return 0
            else:
                return 1+max(left,right)
        dfs(root)
        return res