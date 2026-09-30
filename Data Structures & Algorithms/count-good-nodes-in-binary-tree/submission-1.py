# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num_good = 0
        def dfs(node,max_seen):
            nonlocal num_good
            if not node:
                return
            if node.val >= max_seen:
                num_good += 1
            new_max = max(max_seen, node.val)
            dfs(node.left,new_max)
            dfs(node.right,new_max)
        dfs(root,-101)
        return num_good

            