class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
    
        str1 = strs[0]

        for i in range(len(str1)):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != str1[i]:
                    return str1[:i]
        
        return str1