from collections import defaultdict
import heapq
class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        graph = [[] for _ in range(n)]
        for u, v, times in roads:
            graph[u].append((v,times))
            graph[v].append((u,times))
        dist = [float('inf')] * n
        way = [0] * n
        dist[0] = 0
        way[0] = 1
        pq = []
        heapq.heappush(pq, (0,0))
        while pq:
            curr_times, u = heapq.heappop(pq)
            if curr_times > dist[u]:
                continue
            for v, road_times in graph[u]:
                new_times = curr_times + road_times
                if new_times < dist[v]:
                    dist[v] = new_times
                    way[v] = way[u]
                    heapq.heappush(pq, (new_times, v))
                elif new_times == dist[v]:
                    way[v] = (way[v] + way[u]) % MOD
        return way[n-1]                       