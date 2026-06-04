class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        mem = {}
        def dfs(i: int, c: int) -> int:
            if (i, c) in mem:
                return mem[(i,c)]
            if i >= len(costs):
                return 0
            
            res = []
            if c != 0:
                res.append(costs[i][0] + dfs(i + 1, 0))
            if c != 1:
                res.append(costs[i][1] + dfs(i + 1, 1))
            if c != 2:
                res.append(costs[i][2] + dfs(i + 1, 2))
            
            mem[(i,c)] = min(res)
            return mem[(i,c)]
        
        return min(
            costs[0][0] + dfs(1, 0),
            costs[0][1] + dfs(1, 1),
            costs[0][2] + dfs(1, 2)
        )

        # costs = [[17,2,17],[16,16,5],[14,3,19]]

        # 17 + dfs(1, 0)
        #     16 + dfs(2,1)
        #         14,
        #         19
        #     5  + dfs(2,2)
        #         14
        #         3

        # 2 + dfs(1, 1)
        #     16 + dfs(2, 0)

        #     5  + dfs(2, 2)

        # 17 + dfs(1,2)
