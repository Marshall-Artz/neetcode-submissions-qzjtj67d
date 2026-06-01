class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        cur = self.trie
    
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        
        cur['#'] = True # Marker for end of word

    def search(self, word: str) -> bool:
        cur = self.trie

        for char in word:
            if char not in cur:
                return False
            cur = cur[char]
        
        if '#' not in cur:
            return False
        
        return True

    def startsWith(self, word: str) -> bool:
        cur = self.trie

        for char in word:
            if char not in cur:
                return False
            cur = cur[char]
        
        return True