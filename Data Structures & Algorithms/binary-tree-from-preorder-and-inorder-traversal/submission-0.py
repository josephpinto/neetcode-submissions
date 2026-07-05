# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        next_root = TreeNode(preorder[0])
        inorder_idx = inorder.index(next_root.val)
        inorder_left = inorder[:inorder_idx]
        inorder_right = inorder[inorder_idx+1:]
        preorder_left = preorder[1:1+len(inorder_left)]
        preorder_right = preorder[len(preorder_left)+1:]

        next_root.left = self.buildTree(preorder_left,inorder_left)
        next_root.right = self.buildTree(preorder_right,inorder_right)

        return next_root