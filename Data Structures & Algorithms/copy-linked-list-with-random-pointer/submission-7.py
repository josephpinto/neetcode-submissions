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
        # map of original class ref to copy
        copies_by_original = {}
        dummy = curr = Node(-1)
        while head:
            head_copy = None
            random_copy = None
            if head not in copies_by_original:
                head_copy = Node(head.val)
                copies_by_original[head] = head_copy
            if head.random and head.random not in copies_by_original:
                random_copy = Node(head.random.val)
                copies_by_original[head.random] = random_copy
            random_copy = copies_by_original.get(head.random,None)
            head_copy = copies_by_original[head]
            curr.next = head_copy
            head_copy.random = random_copy
            curr = curr.next
            head = head.next
        return dummy.next
            
                