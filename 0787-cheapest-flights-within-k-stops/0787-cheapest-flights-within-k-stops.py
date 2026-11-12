class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        dist = [float("inf")] * n
        dist[src] = 0
        for _ in range(k + 1):
            temp = dist[:]
            for u,v,price in flights:
                if dist[u] != float("inf"):
                    new_cost = dist[u] + price
                    if new_cost < temp[v]:
                        temp[v] = new_cost
            dist = temp
        if dist[dst] == float("inf"):
            return -1

        return dist[dst]
        