# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        chaser = head
        while chaser:
            length += 1
            chaser = chaser.next

        cycles = length // k
        tail = head
        stack = []

        for i in range(cycles):
            prev = None
            cur = head

            j = 0
            while cur:
                print("cur:", cur.val)
                if j == k: break
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                j += 1
            
            if nxt: print("nxt:", nxt.val)

            print("appending:", prev.val, " & head.val:", head.val)
            stack.append(prev)
            stack.append(head)
            
            head = nxt

        print(stack)
        
        res = stack[0]
        stack.pop(0)

        while stack:
            node1 = stack[0]
            stack.pop(0)
            if stack:
                node2 = stack[0]
                node1.next = node2
                stack.pop(0)
        
        if node1:
            node1.next = nxt
        # if node2:
            # print("node2:", node2.val)
        
        return res

