class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        res = Counter(s1)
        
        for i in range(len(s2)):
            if i + len(s1) > len(s2):
                return False

            for j in range(i, i + len(s1)):
                char = s2[j]
                if res[char] == 0:
                    break
                else:
                    res[char] -= 1
            
            print("max(res):", max(res.values()))
            if max(res.values()) == 0:
                return True
            else:
                res = Counter(s1)
        
        return False