# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = currHead = ListNode()
        
        while head:
        
            # see if we should reverse:
            counter = head
            for i in range(k):
                if not counter:
                    # not enough nodes, return early
                    currHead.next = head
                    return dummy.next
                counter = counter.next

            prev = None
            first_in_group = head
            i = 0
            for _ in range(k):
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp
                i += 1
                
            currHead.next = prev
            currHead = first_in_group
        return dummy.next