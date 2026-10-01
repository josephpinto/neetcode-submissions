# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) >= 2:
            first,second = lists.pop(), lists.pop()
            lists.append(self.mergeTwoLists(first,second))
        return lists[0]

    def mergeTwoLists(self,l1,l2):
        if not l1 and not l2:
            return None
        dummy = curr = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next
