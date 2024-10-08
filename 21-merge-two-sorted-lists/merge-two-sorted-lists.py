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
        if not temp1:
            if not temp2:
                return None
            else:
                return temp2
        else:
            if not temp2:
                return temp1
            else:
                while temp1 != None and temp2 != None:
                    if temp1.val < temp2.val:
                        res.next = temp1
                        temp1 = temp1.next
                    else:
                        res.next = temp2
                        temp2 = temp2.next
                    res = res.next         
                if temp1:
                    res.next = temp1
            
                if temp2:
                    res.next = temp2
           
        return dummy.next
        
        
        
        