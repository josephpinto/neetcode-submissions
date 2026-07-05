# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def dfs(node, max_seen):
            nonlocal result
            if not node: return
            if node.val >= max_seen:
                result += 1
            max_seen = max(max_seen, node.val)
            if node.left:
                dfs(node.left,max_seen)
            if node.right:
                dfs(node.right,max_seen)
        
        dfs(root,-101)
        return result