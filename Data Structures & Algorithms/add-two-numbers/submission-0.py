# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        my_list = dummy = ListNode()

        carry = 0
        while l1 or l2:
            curr_sum = self.getVal(l1) + self.getVal(l2) + carry
            carry = 0
            if curr_sum > 9:
                carry = curr_sum // 10
                curr_sum -= 10
            new_node = ListNode(curr_sum)
            my_list.next = new_node
            my_list = my_list.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry > 0:
            new_node = ListNode(carry)
            my_list.next = new_node
            

        return dummy.next    
    
    def getVal(self, node):
        if not node:
            return 0
        return node.val
    
