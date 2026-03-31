class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.i = 0
        res = set()

        s = []
        def dfs(i: int):
            if i >= len(nums):
                res.add(tuple(s.copy()))
                return
            
            # Include value:
            s.append(nums[i])
            dfs(i+1)

            # Exclude value:
            s.pop()
            dfs(i+1)
        
        dfs(self.i)
        return [list(s) for s in res]
