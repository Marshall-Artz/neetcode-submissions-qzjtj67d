# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create dummy node:
        dummy = ListNode()
        dummy.next = head

        # l and r node:
        # (l is one behind so that we can delete real l node)
        l = dummy
        r = head

        # Get right node location
        for i in range(n):
            r = r.next
        
        # Shift whole window to right
        while r:
            l = l.next
            r = r.next
        
        l.next = l.next.next

        return dummy.next