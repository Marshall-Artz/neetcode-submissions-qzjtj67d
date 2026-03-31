class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = [0] * 26
        l = 0
        res = 0
        
        for r in range(len(s)):
            chars[ord(s[r]) - ord("A")] += 1

            if (r - l + 1) - max(chars) > k:
                chars[ord(s[l]) - ord("A")] -= 1
                l += 1
            
            res = max(res, (r - l + 1))

        return res
            