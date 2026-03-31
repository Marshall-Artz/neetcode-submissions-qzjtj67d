class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        self.i = 0

        s = []
        def dfs(i: int):
            print("current i:", i)
            print("current subset:", s)
            if i >= len(candidates):
                if sum(s) == target:
                    res.add(tuple(sorted(s)))
                return
            
            # Include number to subset
            s.append(candidates[i])
            dfs(i + 1)

            # Don't include number to subset:
            s.pop()
            dfs(i + 1)

        dfs(self.i)
        return [list(l) for l in res]
