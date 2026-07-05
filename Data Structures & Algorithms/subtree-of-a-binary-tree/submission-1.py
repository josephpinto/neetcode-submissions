from collections import deque

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

        queue = deque([root])
        while queue:
            node = queue.popleft()
            if self.isSameTree(node, subRoot): return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False

    def isSameTree(self,t1,t2):
        if t1 and not t2 or t2 and not t1:
            return False
        if not t1 and not t2:
            return True
        
        if t1.val != t2.val:
            return False
        return self.isSameTree(t1.left,t2.left) and self.isSameTree(t1.right,t2.right)