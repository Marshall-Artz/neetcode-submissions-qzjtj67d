class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        l = 0
        r = 0

        have = {}
        need = {}
        formed = 0

        # Initialize our have and need hash maps
        for char in t:
            have[char] = 0
            if char in need:
                need[char] += 1
            else:
                need[char] = 1
        
        found = False
        required_total = len(need)

        res = s + " "

        while l < len(s):
            while not formed == required_total and r < len(s):
                if s[r] in need:
                    have[s[r]] += 1
                    if have[s[r]] == need[s[r]]:
                        formed += 1
                r += 1
            if len(s[l:r]) <= len(res) and formed == required_total:
                res = s[l:r]
                found = True
            if s[l] in have and have[s[l]] > 0:
                if have[s[l]] == need[s[l]]:
                    formed -= 1
                have[s[l]] -= 1
            l += 1
        
        if found == False:
            return ""

        return res