class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        res = Counter(s1)

        print(res)
        
        for i in range(len(s2)):
            if i + len(s1) > len(s2):
                return False

            for j in range(i, i + len(s1)):
                char = s2[j]
                if res[char] == 0:
                    print("char:", char, " not in res")
                    break
                else:
                    res[char] -= 1
                    print("subtracted ", char, " from res")
                    print(res)
            
            print("max(res):", max(res.values()))
            if max(res.values()) == 0:
                print("TRUE")
                return True
            else:
                res = Counter(s1)
                print("res:", res)
                print("FALSE")
        
        return False