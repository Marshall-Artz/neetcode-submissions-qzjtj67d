class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars = [0] * 26
        res   = [0] * 26

        for char in s1:
            chars[ord(char) - ord("a")] += 1
        
        print(chars)
        
        for i in range(len(s2)):
            if i + len(s1) > len(s2):
                return False

            for j in range(i, i + len(s1)):
                char = ord(s2[j]) - ord("a")
                res[char] += 1
            
            print("res:", res)
            print("chars:", chars)
            
            if res == chars:
                return True
            else:
                res = [0] * 26
        
        return False