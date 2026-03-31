# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Reverse linked list:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        
        # Reset values:
        head = prev
        prev = None
        
        # Get nodes for replacement:
        toRemoveTail = None
        toRemove = head

        for i in range(n - 1):
            toRemoveTail = toRemove
            toRemove = toRemove.next
        
        # Replace nodes:
        if toRemove != None and toRemoveTail != None:
            toRemoveTail.next = toRemove.next
        elif toRemove != None and toRemoveTail == None:
            head = toRemove.next

        # Reverse linked list:
        while head != None:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        
        # Reset values:
        head = prev
        prev = None

        return head