class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(s: str, openCount: int, closedCount: int):
            print("s:", s)
            if openCount == n and closedCount == n:
                res.append(s)
                return
            
            # Add open parenthesis
            if openCount < n:
                dfs(s + "(", openCount + 1, closedCount)

            # Add closed parenthesis (conditional)
            if openCount > closedCount:
                dfs(s + ")", openCount, closedCount + 1)

        dfs("", 0, 0)
        return res