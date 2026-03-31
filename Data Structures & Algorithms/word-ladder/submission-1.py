class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        WORD    = len(wordList[0])
        graph   = defaultdict(list)
        visited = set()
        queue   = deque()

        def getWildCards(word: str) -> list:
            res = []
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                res.append(pattern)
            return res

        for word in wordList:
            for wildCard in getWildCards(word):
                graph[wildCard].append(word)

        if endWord not in wordList:
            return 0
        
        queue.append(beginWord)
        
        jump = 1
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()

                if word in visited:
                    continue
                if word == endWord:
                    return jump
                
                visited.add(word)

                for wildCard in getWildCards(word):
                    for nextWord in graph[wildCard]:
                        queue.append(nextWord)
            jump += 1
        return 0