# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        dummy = ListNode(-1)
        res = dummy
        while temp1 != None and temp2 != None:
            if temp1.val < temp2.val:
                res.next = ListNode(temp1.val)
                temp1 = temp1.next
            else:
                res.next = ListNode(temp2.val)
                temp2 = temp2.next
            res = res.next         
        while temp1:
            res.next = ListNode(temp1.val)
            temp1 = temp1.next
            res = res.next
        while temp2:
            res.next = ListNode(temp2.val)
            temp2 = temp2.next
            res = res.next
        return dummy.next
        
        
        
        