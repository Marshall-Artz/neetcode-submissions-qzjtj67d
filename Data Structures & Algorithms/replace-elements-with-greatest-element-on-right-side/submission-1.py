class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = -1
        curr = arr[-1]
        rev = arr[::-1]
        for i in range(len(rev)):
            rev[i] = mx
            if curr > mx:
                mx = curr
            if i+1 < len(rev):
                curr = rev[i+1]
        return rev[::-1]