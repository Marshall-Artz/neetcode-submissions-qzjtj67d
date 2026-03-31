class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        mem = {}
        def dfs(pos1: int, pos2: int) -> int:
            if (pos1, pos2) in mem:
                return mem[(pos1, pos2)]
            elif pos1 >= len(word1):
                return len(word2) - pos2
            elif pos2 >= len(word2):
                return len(word1) - pos1
            
            if word1[pos1] == word2[pos2]:
                mem[(pos1, pos2)] = dfs(pos1 + 1, pos2 + 1)
            else:
                insert  = 1 + dfs(pos1, pos2 + 1)
                delete  = 1 + dfs(pos1 + 1, pos2)
                replace = 1 + dfs(pos1 + 1, pos2 + 1)
                mem[(pos1, pos2)] = min(insert, delete, replace)
            
            return mem[(pos1, pos2)]
        
        return dfs(0, 0)
