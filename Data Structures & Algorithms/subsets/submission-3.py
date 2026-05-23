class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []

        def dfs(i: int) -> None:
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # Add no number:
            dfs(i + 1)

            # Add this number:
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
        
        dfs(0)
        return res

        # nums       = [1,2,3]
        # res        = [[1]]
        # subset     = [1]
        # i, nums[i] = 0, 1