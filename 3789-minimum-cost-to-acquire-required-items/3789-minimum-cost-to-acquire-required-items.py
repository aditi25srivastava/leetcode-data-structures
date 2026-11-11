class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        common = min(need1, need2)
        common_cost = min(costBoth,cost1 + cost2)
        total = common * common_cost
        remaining1 = need1 - common
        remaining2 = need2 - common
        total += remaining1 * min(cost1, costBoth)
        total += remaining2 * min(cost2, costBoth)  
        return total  
        