class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.i = 0

        s = []
        def dfs(i: int):
            if sum(s) == target:
                res.append(s.copy())
                return
            if i >= len(candidates):
                return
            
            # Include number to subset
            s.append(candidates[i])
            dfs(i + 1)

            # Don't include number to subset:
            s.pop()
            while i+1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(i + 1)

        dfs(self.i)
        return res
