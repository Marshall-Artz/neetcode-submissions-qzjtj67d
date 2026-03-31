# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        dummy.next = head
        length = 1

        lengthChaser = head
        while lengthChaser.next != None:
            length += 1
            lengthChaser = lengthChaser.next
        
        print(length)

        midTail = None
        mid = head

        for i in range(math.ceil(length / 2)):
            midTail = mid
            mid = mid.next
        
        # print("mid",mid.val)
        print("midTail:", midTail.val)

        midTail.next = None

        midPrev = None

        while mid:
            midNext = mid.next
            mid.next = midPrev
            midPrev = mid
            mid = midNext
        
        # print("mid at end?:",midPrev.val)

        node1 = head
        node1Next = None
        node2 = midPrev
        node2Next = None

        while node1 and node2:
            node1Next = node1.next
            node2Next = node2.next
            node1.next = node2
            node2.next = node1Next
            node1 = node1Next
            node2 = node2Next


        