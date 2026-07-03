# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = r = head

        for _ in range(n):
            r = r.next
        
        prev_l = dummy = ListNode(0,head)
        while r:
            r = r.next
            prev_l, l = l, l.next
        
        prev_l.next = l.next
        
        return dummy.next