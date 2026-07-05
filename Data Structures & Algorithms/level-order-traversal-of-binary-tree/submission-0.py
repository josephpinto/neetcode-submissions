from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root,0)])

        result = []
        curr_level = 0
        while queue:
            level_list = []
            while queue and queue[0][1] == curr_level:
                node, _ = queue.popleft()
                if node.left:
                    queue.append((node.left,curr_level+1))
                if node.right:
                    queue.append((node.right,curr_level+1))
                level_list.append(node.val)
            result.append(level_list)
            curr_level += 1
        return result


