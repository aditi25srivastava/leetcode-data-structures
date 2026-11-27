class Solution(object):
    def maximumSaleItems(self, items, budget):
        """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
        n = len(items)
        bonus = [0] * n
        for i in xrange(n):
            cnt = 0
            for j in xrange(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    cnt += 1
            bonus[i] = cnt

        dp = [0] * (budget + 1)
        for i in xrange(n):
            cost = items[i][1]
            free_copies = bonus[i]
            if cost <= budget:
                for b in xrange(budget, cost - 1, -1):
                    cand = dp[b - cost] + 1 + free_copies
                    if cand > dp[b]:
                        dp[b] = cand
                for b in xrange(cost, budget + 1):
                    cand = dp[b - cost] + 1
                    if cand > dp[b]:
                        dp[b] = cand

        return max(dp)
        