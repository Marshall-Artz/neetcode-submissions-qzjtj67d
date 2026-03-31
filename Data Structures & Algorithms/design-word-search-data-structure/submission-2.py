class WordDictionary:

    def __init__(self):
        self.dic = {}
    
    def dfs(self, searchDic: dict, word: str) -> bool:
        if not word:
            if '#' not in searchDic:
                return False
            else:
                return True
        
        if word[0] == '.':
            for key in searchDic.keys():
                if key != '#':
                    if self.dfs(searchDic[key], word[1:]):
                        return True
            return False
        
        if word[0] not in searchDic:
            return False
        
        return self.dfs(searchDic[word[0]], word[1:])

    def addWord(self, word: str) -> None:
        cur = self.dic
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur['#'] = True
        print(self.dic)

    def search(self, word: str) -> bool:
        return self.dfs(self.dic, word)
