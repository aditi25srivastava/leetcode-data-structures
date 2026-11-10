class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for i in range(n + 1):
            for j in range(i  + 1, min(i + 4, n + 1)):
                new_cost = dp[i] + costs[j- 1] + (j - i)**2
                dp[j] = min(dp[j], new_cost)
        return dp[n]            
            
        