class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        total = sum(matchsticks)
        side  = total / 4

        if total % 4 != 0:
            return False

        s1, s2, s3, s4 = 0, 0, 0, 0

        def dfs(pos: int) -> bool:
            nonlocal s1, s2, s3, s4
            if pos >= len(matchsticks):
                return True
            
            match = matchsticks[pos]

            # First bucket:
            s1 += match
            c1 = dfs(pos + 1) if s1 <= side else False
            s1 -= match

            # Second bucket:
            s2 += match
            c2 = dfs(pos + 1) if s2 <= side else False
            s2 -= match

            # Third bucket:
            s3 += match
            c3 = dfs(pos + 1) if s3 <= side else False
            s3 -= match

            # Fourth bucket:
            s4 += match
            c4 = dfs(pos + 1) if s4 <= side else False
            s4 -= match

            return c1 or c2 or c3 or c4
        
        return dfs(0)

        # matchsticks    = [1,3, 4,2,2,4]
        # total = 16
        # side  = 4
        # pos   = 2
        # match = 4
        # s1, s2, s3, s4 = 4, 4, 0, 0
        # c1, c2, c3, c4 = F, F, F, F
