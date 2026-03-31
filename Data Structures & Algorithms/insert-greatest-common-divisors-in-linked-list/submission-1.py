# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def getGCD(a, b):
            while b > 0:
                a, b = b, a % b
            return a
        
        n1 = head
        n2 = head.next

        while n2:
            newNode = ListNode(getGCD(n1.val, n2.val))
            n1.next = newNode
            newNode.next = n2

            n1 = n2
            n2 = n2.next
        
        return head
