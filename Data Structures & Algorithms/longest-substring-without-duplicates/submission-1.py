class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l   = 0
        r   = 0
        mx  = 1
        lmx = 1

        st = set()

        if len(s) == 0:
            return 0

        while True:
            st.add(s[r])

            if r+1 < len(s) and s[r+1] not in st:
                r += 1
                lmx += 1
                mx = max(mx, lmx)
            elif r+1 < len(s) and s[r+1] in st and l != r:
                st.remove(s[l])
                l += 1
                lmx -= 1
            elif r+1 < len(s) and s[r+1] in st and l == r:
                l += 1
                r += 1
            else:
                break
            
        
        return mx