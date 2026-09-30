# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return not subRoot
        res = False
        def dfs(node):
            nonlocal res
            if res or not node:
                 return
            if self.isSameTree(node,subRoot):
                res = True
                return
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res
    
    def isSameTree(self,p,q):
        def dfs(p,q):
            if not p and not q:
                return True
            if p and not q:
                return False
            if q and not p:
                return False
            if q.val != p.val:
                return False
            return dfs(p.left,q.left) and dfs(p.right,q.right)
        return dfs(p,q)