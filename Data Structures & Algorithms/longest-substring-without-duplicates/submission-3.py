class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        l, r  = 0, 0
        chars = set()

        subs = 1

        while r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
                subs = max(subs, r - l + 1)
                r += 1
            else:
                chars.remove(s[l])
                l += 1
        
        return subs

        # s = abcabc b b
        # chars = {
        #     b
        # }
        # l, s[l] = 7, b
        # r, s[r] = 8, b
        # subs    = 3