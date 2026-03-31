# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        
        res = []
                
        while True:
            if len(lists) % 2 == 1:
                lists.append(None)

            for i in range(0, len(lists), 2):
                node1 = lists[i]
                node2 = lists[i+1]
                dummy = ListNode(-1)
                head  = dummy

                while node1 and node2:
                    if node1.val <= node2.val:
                        head.next = node1
                        head = head.next
                        node1 = node1.next
                    elif node1.val > node2.val:
                        head.next = node2
                        head = head.next
                        node2 = node2.next
                
                head.next = node1 or node2
                
                res.append(dummy.next)
            
            if len(res) == 1:
                break

            lists = res
            res   = []
        
        return res[0]