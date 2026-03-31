class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = {}
        self.head = Node(-1, -1)
        self.tail = self.head

    def remove(self, node):
        prv, nxt = node.prev, node.next
        if prv: prv.next = nxt
        if nxt: nxt.prev = prv
        if node == self.tail: self.tail = prv

    def insert(self, node):
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

    def get(self, key: int) -> int:
        if key in self.dic:
            n = self.dic[key]
            self.remove(n)
            self.insert(n)
            return n.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.remove(self.dic[key])
        elif len(self.dic) == self.cap:
            lru = self.head.next
            del self.dic[lru.key]
            self.remove(lru)

        n = Node(key, value)
        self.dic[key] = n
        self.insert(n)