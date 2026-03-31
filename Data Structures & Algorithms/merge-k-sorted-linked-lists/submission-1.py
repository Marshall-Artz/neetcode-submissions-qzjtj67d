# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        dummy = ListNode()
        head  = dummy
        minNode = (0, lists[0])

        while True:
            minNode = (-1, None)

            for i, node in enumerate(lists):
                if node and minNode[1] == None:
                    minNode = (i, node)
                elif node and minNode[1] and node.val < minNode[1].val:
                    minNode = (i, node)
            
            if minNode[1]:
                lists[minNode[0]] = lists[minNode[0]].next
                head.next = minNode[1]
                head = head.next
            else:
                break
        
        return dummy.next