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
        nodeMap = {} # original node : copy node

        first_pass = head
        
        while first_pass:
            copy_node = Node(first_pass.val)
            nodeMap[first_pass] = copy_node
            my_list.next = copy_node
            my_list, first_pass = my_list.next, first_pass.next
        
        second_pass = head
        my_list = dummy.next
        while second_pass:
            if second_pass.random in nodeMap:
                my_list.random = nodeMap[second_pass.random]
            second_pass, my_list = second_pass.next, my_list.next

        return dummy.next