# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        mergeHead = ListNode()
        start = mergeHead
        
        while list1 and list2:
            if list1.val < list2.val:
                mergeHead.next = list1
                list1 = list1.next
            else:
                mergeHead.next = list2
                list2 = list2.next
            mergeHead = mergeHead.next
            
        if list1:
            mergeHead.next = list1
        elif list2:
            mergeHead.next = list2
        return start.next