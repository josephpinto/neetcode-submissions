"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cache = {}

        def dfs(curr):
            if not curr:
                return None
            if curr.val in cache:
                return cache[curr.val]
            newNode = Node(curr.val)
            cache[curr.val] = newNode
            for nei in curr.neighbors:
                newNode.neighbors.append(dfs(nei))
            return newNode
        return dfs(node)


                



