class MyHashSet:

    def __init__(self):
        self.hashSet = [-1] * 10000

    def add(self, key: int) -> None:
        self.hashSet[key % 10000] = key

    def remove(self, key: int) -> None:
        self.hashSet[key % 10000] = -1

    def contains(self, key: int) -> bool:
        return self.hashSet[key % 10000] != -1

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)