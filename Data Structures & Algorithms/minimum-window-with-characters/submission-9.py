class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        def isValid(have, need):
            for key, value in have.items():
                if have[key] < need[key]:
                    return False
            return True

        l = 0
        r = 0

        have = {}
        need = {}
        found = False

        # Initialize our have and need hash maps
        for char in t:
            have[char] = 0
            if char in need:
                need[char] += 1
            else:
                need[char] = 1

        print("have:", have)
        print("need:", need)
        res = s

        while l < len(s):
            print("for:", s[l])
            while not isValid(have, need) and r < len(s):
                print("s[r]:", s[r])
                print("s[l:r]:", s[l:r+1])
                print("l:", l, " r:", r)
                if s[r] in have:
                    have[s[r]] += 1
                    print("added val:", have)
                r += 1
            if len(s[l:r]) <= len(res) and isValid(have, need):
                res = s[l:r]
                found = True
                print("new res:", res)
            if s[l] in have and have[s[l]] > 0:
                have[s[l]] -= 1
                print("removed value:", have)
            l += 1
        
        if found == False:
            return ""

        return res