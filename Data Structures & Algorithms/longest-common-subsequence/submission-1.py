class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        if len(text1) < len(text2):
            temp = text1
            text1 = text2
            text2 = temp

        # Base case:
        # - if pos1 >= len(text1): return 0
        # - Char at pos1 in text2 != char at pos2 in text1
        # Decisions:
        # - if char at pos1 and pos2 are equal:
        #   - increment both, add 1, call recursive function
        # - Else:
        #   - increment pos1
        #   OR
        #   - increment pos2
        mem = {}
        def dfs(pos1: int, pos2: int) -> int:
            if (pos1, pos2) in mem:
                return mem[(pos1, pos2)]
            if pos1 >= len(text1) or pos2 >= len(text2):
                return 0
            if text1[pos1] == text2[pos2]:
                return 1 + dfs(pos1 + 1, pos2 + 1)
            
            # increment pos1 or increment pos2
            mem[(pos1, pos2)] = max(dfs(pos1 + 1, pos2), dfs(pos1, pos2 + 1))
            
            return mem[(pos1, pos2)]
        
        return dfs(0, 0)