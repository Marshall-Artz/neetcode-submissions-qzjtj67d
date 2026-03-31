class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        l, r = 0, 0
        mx = 0

        while r < len(s):
            if s[r] not in st:
                st.add(s[r])
                mx = max(mx, r - l + 1)
                r += 1
            else:
                st.remove(s[l])
                l += 1
        
        return mx