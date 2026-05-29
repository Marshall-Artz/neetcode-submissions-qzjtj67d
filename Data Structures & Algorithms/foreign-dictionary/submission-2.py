class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}

        # Populate graph with empty lists
        for word in words:
            for char in word:
                adj[char] = []

        # Populate graph
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            j, k = 0, 0
            while j < len(word1) and k < len(word2):
                char1, char2 = word1[j], word2[k]

                if char1 != char2:
                    adj[char1].append(char2)
                    break

                j += 1
                k += 1
            else:
                if len(word1) > len(word2):
                    return ""
        
        # Traverse Graph:
        res = ""
        def traverse() -> str:
            nonlocal res
            gVisit = set()
            lVisit = set()

            def dfs(char: str) -> bool:
                nonlocal res

                if char in lVisit:
                    return True
                if char in gVisit:
                    return False
                
                lVisit.add(char)
                gVisit.add(char)
                
                for nextChar in adj[char]:
                    if dfs(nextChar):
                        return True
                
                lVisit.remove(char)
                
                res = res + char
                return False

            for word in words:
                for char in word:
                    if char not in gVisit:
                        if dfs(char):
                            return ""
            return "ok"
        
        if traverse() == "":
            return ""
        return res[::-1]

        # words =  ["hrn","hrf","er","enn","rfnn"]
        # adj = {
        #     "n": ["f"],
        #     "h": ["e"],
        #     "r": ["n"],
        #     "e": ["r"]
        # }
        # word1, word2 = "hrn", "hrne"
        # j, word1[j], k, word2[k] = 3, "", 3, "e"
