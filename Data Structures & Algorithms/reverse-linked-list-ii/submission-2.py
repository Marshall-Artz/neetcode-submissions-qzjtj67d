# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        prev = None
        cur  = head

        for i in range(1, left):
            prev = cur
            cur  = cur.next
        
        leftTail = prev
        reverseTail = cur
        prev = None

        for i in range(left, right + 1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        rightNxt = cur
        
        if leftTail:
            leftTail.next = prev
        else:
            head = prev

        reverseTail.next = rightNxt

        return head