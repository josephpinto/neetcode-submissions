# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr_head = dummy = ListNode()

        while head:
            counterNode = head
            for _ in range(k):
                if not counterNode:
                    # less than k, skip rest and return
                    curr_head.next = head
                    return dummy.next
                counterNode = counterNode.next
            prev = None
            # will become our new curr head
            first_in_group = head
            for _ in range(k):
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp
            curr_head.next = prev
            curr_head = first_in_group
        return dummy.next
