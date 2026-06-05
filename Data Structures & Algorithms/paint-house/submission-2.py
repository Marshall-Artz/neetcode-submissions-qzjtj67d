class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        dp = costs.copy()

        for i in range(1, len(costs)):
            dp[i][0] += min(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] += min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] += min(dp[i - 1][0], dp[i - 1][1])
        
        return min(dp[-1])

        # costs = [
        #     [17,2,17],
        #     [16,16,5],
        #     [14,3,19]
        # ]
        # dp = [
        #     [17,2,17],
        #     [18,33,7],
        #     [21,10,37]
        # ]