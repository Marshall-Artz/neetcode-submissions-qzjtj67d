class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = [0] * 26
        l = 0
        res = 0
        
        for r in range(len(s)):
            chars[ord(s[r]) - ord("A")] += 1
            print(s[l:r+1])
            print("length:", (r - l + 1))
            print("max(chars):", max(chars))
            print("k:", k)
            print(chars)

            while (r - l + 1) - max(chars) > k:
                print(ord(s[l]) - ord("A"))
                chars[ord(s[l]) - ord("A")] -= 1
                l += 1
            print()
            
            res = max(res, (r - l + 1))
        
        print(chars)

        return res
            