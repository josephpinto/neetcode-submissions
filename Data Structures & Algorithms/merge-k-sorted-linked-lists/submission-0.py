# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1:
            return lists[0]
        if not lists:
            return None

        while len(lists) > 1:
            list1, list2 = lists.pop(), lists.pop()
            new_list = self.mergeTwoLists(list1,list2)
            lists.append(new_list)
        
        return lists[0]
    
    def mergeTwoLists(self, l1, l2):
        dummy = new_list_head = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                new_list_head.next = l1
                l1 = l1.next
            else:
                new_list_head.next = l2
                l2 = l2.next
            new_list_head = new_list_head.next
        
        if l1:
            new_list_head.next = l1
        if l2:
            new_list_head.next = l2
        return dummy.next
