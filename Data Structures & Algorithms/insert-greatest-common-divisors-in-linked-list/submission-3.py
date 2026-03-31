# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def getGCD(val1: int, val2: int) -> int:
            small = min(val1, val2)
            large = max(val1, val2)

            n = small

            while small % n != 0 or large % n != 0:
                n -= 1
                
            return n
        
        n1 = head
        n2 = head.next

        while n2:
            n1.next = ListNode(getGCD(n1.val, n2.val))
            n1.next.next = n2

            n1 = n2
            n2 = n2.next
        
        return head
