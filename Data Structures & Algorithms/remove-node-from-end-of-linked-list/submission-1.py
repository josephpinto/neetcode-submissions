# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        size = 0

        counter_node = head

        while counter_node:
            size +=1
            counter_node = counter_node.next
        
        removal_node = head
        removal_prev = ListNode(0, head)
        dummy = removal_prev

        required_steps = size - n
        while required_steps > 0:
            removal_prev, removal_node = removal_node, removal_node.next
            required_steps -= 1

        removal_prev.next = removal_node.next

        return dummy.next