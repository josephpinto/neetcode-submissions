"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {}
        dummy = my_list = Node(-1)

        while head:
            curr_copy_node = self.getNode(head,copies)
            next_node = self.getNode(head.next,copies)
            random_node = self.getNode(head.random,copies)
            curr_copy_node.next = next_node
            curr_copy_node.random = random_node
            my_list.next = curr_copy_node
            
            head = head.next
            my_list = my_list.next
        return dummy.next

    def getNode(self, node, node_map):
        if not node: return None
        if node in node_map:
            return node_map[node]
        new_node = Node(node.val)
        node_map[node] = new_node
        return new_node
