class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        i   = 0

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return []

            # Add current value
            subset.append(nums[i])
            print("new subset:", subset)
            dfs(i + 1)

            # Don't add current value
            subset.pop()
            print("subset without:", subset)
            dfs(i + 1)

        dfs(i)
        return res