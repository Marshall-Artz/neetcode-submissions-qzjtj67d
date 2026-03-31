"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        dummy.next = head
        dic = {}

        if head == None:
            return None

        while head:
            dic[head] = Node(head.val)
            head = head.next
        
        head = dummy.next

        while head:
            copyNode = dic[head]
            if head.next:
                copyNode.next = dic[head.next]
            if head.random:
                copyNode.random = dic[head.random]
            prev = head
            head = head.next

        return dic[dummy.next]