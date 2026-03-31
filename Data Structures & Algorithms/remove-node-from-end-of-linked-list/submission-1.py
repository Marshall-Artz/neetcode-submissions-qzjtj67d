# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        
        toRemoveTail = None
        toRemove = prev

        for i in range(n - 1):
            toRemoveTail = toRemove
            toRemove = toRemove.next
        
        print("toRemoveTail:", toRemoveTail)
        print("toRemove:", toRemove)
        
        if toRemove != None and toRemoveTail != None:
            toRemoveTail.next = toRemove.next
        elif toRemove != None and toRemoveTail == None:
            prev = toRemove.next

        head = prev
        prev = None

        while head != None:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt

        return prev