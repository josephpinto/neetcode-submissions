# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        is_balanced = True

        def dfsHeight(root):
            nonlocal is_balanced
            if not is_balanced: return 0
            if not root: return 0
            hl,hr = dfsHeight(root.left), dfsHeight(root.right)
            if abs(hl-hr) > 1:
                is_balanced = False
            return max(hl,hr)+1

        dfsHeight(root)


        return is_balanced
        
