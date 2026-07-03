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
        my_list = dummy =  Node(0)
        node_map = {} # original node : copy node

        first_pass = head
        
        while first_pass:
            copy_curr_node = self.getNode(node_map, first_pass)
            copy_next_node = self.getNode(node_map, first_pass.next)
            copy_random_node = self.getNode(node_map, first_pass.random)
            
            copy_curr_node.next = copy_next_node
            copy_curr_node.random = copy_random_node
            
            my_list.next = copy_curr_node
            my_list, first_pass = my_list.next, first_pass.next

        return dummy.next
    def getNode(self, node_map, key_node):
        if not key_node: return None
        if key_node in node_map:
            return node_map[key_node]
        new_node = Node(key_node.val)
        node_map[key_node] = new_node
        return new_node
