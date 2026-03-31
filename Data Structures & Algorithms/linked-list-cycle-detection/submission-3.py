# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head
        f = head
        while s and f != None:
            s = s.next
            f = f.next
            if f != None:
                f = f.next
            else:
                break
            if s == f:
                return True
        
        return False