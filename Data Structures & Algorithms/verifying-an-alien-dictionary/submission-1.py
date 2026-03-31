class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}

        for i, char in enumerate(order):
            dic[char] = i
        
        def dfs(pos: int) -> bool:
            if pos == len(words) - 1:
                return True
            
            word1, word2 = words[pos], words[pos + 1]
            i, j = 0, 0

            while i < len(word1) and j < len(word2):
                print(word1, word2)
                print("dic[word1[", i, "]]:", dic[word1[i]], word1[i], "dic[word2[", j, "]]:", dic[word2[j]], word2[j])
                if dic[word1[i]] > dic[word2[j]]:
                    return False
                elif dic[word1[i]] < dic[word2[j]]:
                    return dfs(pos + 1)
                    break
                i += 1
                j += 1
            
            if i < len(word1) and j >= len(word2):
                return False
            
            return dfs(pos + 1)
        
        return dfs(0)