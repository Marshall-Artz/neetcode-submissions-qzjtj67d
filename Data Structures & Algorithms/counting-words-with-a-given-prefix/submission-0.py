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

    def isPrefix(self, word: str) -> bool:
        cur = self.trie
        for char in word:
            if char not in cur:
                return False
            cur = cur[char]
        
        return True

    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            self.insert(word)
            count += self.isPrefix(pref)
            self.trie.clear()
        
        return count
    
    # words = ["neetcode","neet","nee","code"], pref = "ne"
    # self.trie = {
    #     "n": {
    #         "e": {
    #             "e": {
    #                 "t": {
    #                     "c": {
    #                         "o": {
    #                             "d": {
    #                                 "e" {
    #                                     "#": True
    #                                 }
    #                             }
    #                         }
    #                     }
    #                 }
    #             }
    #         }
    #     }
    # }