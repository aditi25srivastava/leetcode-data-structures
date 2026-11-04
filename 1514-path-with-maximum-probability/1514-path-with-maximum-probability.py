import heapq
class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        graph = [[] for _ in range(n)]
        for i, (u,v) in enumerate(edges):
            p = succProb[i]
            graph[u].append((v,p))
            graph[v].append((u,p))
            
            prob = [0.0] * n
            prob[start_node] = 1.0
            pq = [(-1.0, start_node)]
    
        while pq:
            curr_prob, node = heapq.heappop(pq)
            curr_prob = -curr_prob
            if node == end_node:
                return curr_prob
            if curr_prob < prob[node]:
                continue

            for neighbor, edge_prob in graph[node]:
                new_prob = curr_prob * edge_prob
                if new_prob > prob[neighbor]:
                    prob[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))

                    
        return prob[end_node]                




        
    

       