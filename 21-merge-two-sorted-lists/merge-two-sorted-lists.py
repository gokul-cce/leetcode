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
        while temp1 != None or temp2 != None:
            if temp1 and temp2:
                if temp1.val < temp2.val:
                    new_node = ListNode(temp1.val)
                    res.next = new_node
                    res = res.next
                    temp1 = temp1.next
                else:
                    new_node = ListNode(temp2.val)
                    res.next = new_node
                    res = res.next
                    temp2 = temp2.next
                continue
            if temp1:
                new_node = ListNode(temp1.val)
                res.next = new_node
                temp1 = temp1.next
                res = res.next
            if temp2:
                new_node = ListNode(temp2.val)
                res.next = new_node
                temp2 = temp2.next
                res = res.next
        return dummy.next
        
        
        
        