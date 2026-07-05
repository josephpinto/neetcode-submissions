from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root: return result

        queue = deque([root])

        while queue:
            numInLevel = len(queue)
            for i in range(numInLevel):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                # last in level
                if i == numInLevel - 1:
                    result.append(node.val)




        return result

