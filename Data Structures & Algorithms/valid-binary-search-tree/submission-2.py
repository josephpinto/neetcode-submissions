# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, curr_min, curr_max):
            if not root:
                return True
            
            isLeftValid = isRightValid = True
            isCurrValid = curr_min <  root.val < curr_max
            if root.left:
                isLeftValid = dfs(root.left, curr_min, min(curr_max, root.val))
            if root.right:
                isRightValid = root.right.val > root.val and dfs(root.right, max(curr_min, root.val), curr_max)
            return isLeftValid and isRightValid and isCurrValid
        return dfs(root, float('-inf'),float('inf'))

        