import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = [[] for _ in range(n + 1)]
        for u,v,w in times:
            graph[u].append((v,w))
        dist = [float('inf')] * (n + 1)
        qp = [(0, k)]
        dist[k] = 0
        while qp:
            curr_time, node = heapq.heappop(qp)
            if curr_time > dist[node]:
                continue
            for neighbor, weight in graph[node]:
                new_time = curr_time + weight
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(qp, (new_time, neighbor))
        max_time = max(dist[1:])
        return max_time if max_time != float("inf") else -1         
        
        