class Solution:
    def __init__(self):
        self.trie = {}
    
    def insert(self, word: str) -> None:
        cur = self.trie

        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        
        cur['#'] = True
    
    def isPrefix(self, word1: str, word2: str) -> bool:
        self.trie.clear()
        self.insert(word2)

        cur = self.trie
        for char in word1:
            if char not in cur:
                return False
            cur = cur[char]
        
        return True
    
    def isSuffix(self, word1: str, word2: str) -> bool:
        return self.isPrefix(word1[::-1], word2[::-1])
    
    def isPrefixAndSuffix(self, word1: str, word2: str) -> bool:
        return self.isPrefix(word1, word2) and self.isSuffix(word1, word2)

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0

        for i, word1 in enumerate(words):
            for j in range(i + 1, len(words)):
                word2 = words[j]

                if self.isPrefixAndSuffix(word1, word2):
                    count += 1

        return count