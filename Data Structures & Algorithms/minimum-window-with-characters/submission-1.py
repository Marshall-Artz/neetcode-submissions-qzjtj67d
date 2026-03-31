class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0

        if len(t) > len(s):
            return ""

        dic = Counter(t)
        edit = dic
        shortest = s
        found = False

        print(dic)

        for l in range(len(s)):
            if s[l] in dic:
                cur = ""
                edit = dic.copy()
                
                for r in range(l, len(s)):
                    cur += s[r]
                    print("edit:", edit)
                    print("l:", l, " r:", r)
                    print("Cur:", cur)
                    if len(shortest) > 0 and len(cur) > len(shortest):
                        print("Cur longer than shortest, break")
                        break

                    if s[r] in edit and edit[s[r]] >= 1:
                        edit[s[r]] -= 1
                        print("removed:", edit)
                    
                    if max(edit.values()) == 0:
                        print("NEW SHORTEST:", cur)
                        if len(cur) <= len(shortest):
                            shortest = cur
                            found = True
                        break
                    
        if found == False:
            return ""
        
        return shortest