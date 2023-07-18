# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return head

        count = 0
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        prev = None
        i=0
        while curr != None:
            i += 1
            curr = curr.next

        curr = head

        while count < k%i:
            while (curr.next != None):
                prev = curr
                curr = curr.next

            curr.next = dummy.next
            dummy.next = curr
            prev.next = None
            count += 1
        
        return dummy.next