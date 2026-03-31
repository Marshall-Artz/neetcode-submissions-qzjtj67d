class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        print("CAP:", capacity)
        self.cap = capacity
        self.dic = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self, node):
        prv = self.tail.prev
        prv.next = node
        self.tail.prev = node
        node.prev = prv
        node.next = self.tail
    
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next = node.next
        nxt.prev = node.prev

    def get(self, key: int) -> int:
        print("GET:", key)
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            self.insert(node)

            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        print("PUT:", key, " -> ", value)

        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        elif len(self.dic) == self.cap:
            removeNode = self.head.next
            insertNode = Node(key, value)
            self.dic.pop(removeNode.key)
            self.remove(removeNode)
            self.insert(insertNode)
            self.dic[key] = insertNode
        else:
            node = Node(key, value)
            self.insert(node)
            self.dic[key] = node
