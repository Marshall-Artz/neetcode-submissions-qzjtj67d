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
        mod = 10

        while l1 or l2:
            if l1 and l2 == None:
                val1, val2 = l1.val, 0
            elif l1 == None and l2:
                val1, val2 = 0, l2.val
            else:
                val1, val2 = l1.val, l2.val

            print("val1:", val1)
            print("val2:", val2)

            dummy.next = ListNode((val1 + val2 + rem) % 10)
            dummy = dummy.next
            rem = (val1 + val2 + rem) // 10

            print("dummy.val:", dummy.val)
            print("remainder:", rem)

            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if rem:
            dummy.next = ListNode(rem)
        
        return head.next