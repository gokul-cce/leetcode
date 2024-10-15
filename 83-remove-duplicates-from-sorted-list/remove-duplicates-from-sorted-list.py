# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        dup = set()
        while temp != None:
            if temp.val in dup:
                prev.next = temp.next
                

            else:
                dup.add(temp.val)
                prev = temp
            temp = temp.next
        return head

        