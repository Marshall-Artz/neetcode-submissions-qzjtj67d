class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        subsets = []
        subset  = []
        def dfs(pos: int):
            if pos >= len(nums):
                subsets.append(subset.copy())
                return
            
            # Don't include:
            dfs(pos + 1)

            # Include:
            subset.append(nums[pos])
            dfs(pos + 1)
            subset.pop()
        
        dfs(0)

        xor = 0

        for i, subset in enumerate(subsets):
            xor = 0
            for num in subset:
                xor = xor ^ num
            subsets[i] = xor

        return sum(subsets)
            