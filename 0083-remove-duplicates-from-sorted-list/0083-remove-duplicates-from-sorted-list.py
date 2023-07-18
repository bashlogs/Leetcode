# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        prev = dummy
        

        while curr is not None:
            if curr.next is not None and curr.val == curr.next.val:
                while curr.next is not None and curr.val == curr.next.val:
                    curr = curr.next
                    prev.next = curr
            else:
                prev = prev.next
                
            prev = curr            
            curr = curr.next
        return dummy.next