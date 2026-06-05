class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        dp = [costs[0][0], costs[0][1], costs[0][2]]

        for i in range(1, len(costs)):
            red = min(dp[1], dp[2]) + costs[i][0]
            blue = min(dp[0], dp[2]) + costs[i][1]
            green = min(dp[0], dp[1]) + costs[i][2]

            dp[0], dp[1], dp[2] = red, blue, green
        
        return min(dp)

        # costs = [
        #     [17,2,17],
        #     [16,16,5],
        #     [14,3,19]
        # ]
        # dp = [18,2,17]

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