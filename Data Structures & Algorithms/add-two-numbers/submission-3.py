# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        rem = 0

        l1i = l1
        l2i = l2
        
        # Create 0s at None values
        while l1i or l2i:
            if l1i.next and l2i.next == None:
                l2i.next = ListNode(0)
            elif l1i.next == None and l2i.next:
                l1i.next = ListNode(0)
            l1i = l1i.next
            l2i = l2i.next
        
        while l1 and l2:
            dummy.next = ListNode((l1.val + l2.val + rem) % 10)
            rem = (l1.val + l2.val + rem) // 10

            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        
        if rem != 0:
            dummy.next = ListNode(rem)
        
        return head.next