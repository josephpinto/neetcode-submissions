# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in order traversal, return index [k]
        visited_count = 0
        res = None
        def inOrder(root):
            nonlocal visited_count, res
            if not root or res: return

            inOrder(root.left)
            visited_count += 1
            if visited_count == k:
                res = root.val
            inOrder(root.right)

        inOrder(root)
        return res