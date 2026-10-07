# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = curr_head = ListNode()

        while head:
            # check if there's at least k nodes left
            counter = head
            for _ in range(k):
                if not counter:
                    curr_head.next = head
                    return dummy.next
                counter = counter.next
            next_curr_head = head
            prev = None
            for _ in range(k):
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp
            curr_head.next = prev
            curr_head = next_curr_head
        

        return dummy.next