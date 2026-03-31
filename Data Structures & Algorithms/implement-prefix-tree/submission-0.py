class PrefixTree:

    def __init__(self):
        self.dic = {}

    def insert(self, word: str) -> None:
        cur = self.dic
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur['#'] = True
        print("dic after (", word, "):", self.dic)


    def search(self, word: str) -> bool:
        cur = self.dic
        for char in word:
            if char not in cur:
                return False
            cur = cur[char]
        
        if '#' not in cur:
            return False
        
        return True

    def startsWith(self, prefix: str) -> bool:
        cur = self.dic
        for char in prefix:
            if char not in cur:
                return False
            cur = cur[char]
        
        return True