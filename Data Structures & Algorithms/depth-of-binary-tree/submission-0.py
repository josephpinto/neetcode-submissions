# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)

    def dfs(self, root, currDepth):
        if not root:
            return currDepth
        return max(self.dfs(root.left, currDepth+1), self.dfs(root.right,currDepth+1))