# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = None
        def dfs(node):
            nonlocal res
            if res:
                return 0
            if not node:
                return 0
            seen_left = dfs(node.left)
            seen_right = dfs(node.right)
            summ = seen_left+seen_right
            if node.val == p.val or node.val == q.val:
                summ += 1
            if summ == 2:
                res = node
                return 0
            return summ
        dfs(root)
        return res
            