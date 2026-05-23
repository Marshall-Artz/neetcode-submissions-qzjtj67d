class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        cur = self.trie
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur['#'] = True

    def search(self, word: str) -> bool:
        cur = self.trie
        for char in word:
            if char not in cur:
                return False
            else:
                cur = cur[char]
        
        return '#' in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for char in prefix:
            if char not in cur:
                return False
            else:
                cur = cur[char]
        
        return True