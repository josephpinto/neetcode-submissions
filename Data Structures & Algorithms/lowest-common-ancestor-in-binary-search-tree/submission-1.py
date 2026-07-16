# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        result = None

        def dfs(node):
            nonlocal result
            if result: return 0
            if not node: return 0
            left_sum, right_sum = dfs(node.left), dfs(node.right)
            curr_node_sum = 1 if node.val == q.val or node.val == p.val else 0
            curr_sum = left_sum + right_sum + curr_node_sum
            if curr_sum == 2:
                result = node
                return 0
            return curr_sum

        dfs(root)
        return result

