class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(st: str) -> bool:
            if st == st[::-1]:
                return True
            else:
                return False

        res = []
        sub = []
        def dfs(i: int) -> bool:
            # Base case stuff
            if i >= len(s):
                res.append(sub.copy())
                return

            for x in range(i, len(s)):
                # print(s[i:x+1])
                if isPalindrome(s[i:x+1]):
                    sub.append(s[i:x+1])
                    dfs(x+1)
                    sub.pop()

        dfs(0)
        return res