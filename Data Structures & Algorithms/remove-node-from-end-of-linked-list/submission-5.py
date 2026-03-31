# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        
        head = prev
        prev = None
        
        toRemoveTail = None
        toRemove = head

        for i in range(n - 1):
            toRemoveTail = toRemove
            toRemove = toRemove.next
        
        print("toRemoveTail:", toRemoveTail)
        print("toRemove:", toRemove)
        
        if toRemove != None and toRemoveTail != None:
            toRemoveTail.next = toRemove.next
        elif toRemove != None and toRemoveTail == None:
            head = toRemove.next

        while head != None:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        
        head = prev
        prev = None

        return head