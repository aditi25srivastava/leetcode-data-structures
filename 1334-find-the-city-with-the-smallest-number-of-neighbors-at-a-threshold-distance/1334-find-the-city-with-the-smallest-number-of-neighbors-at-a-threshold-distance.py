class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u, v, weight in edges:
            dist[u][v] = weight
            dist[v][u] = weight
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] == float('inf') or dist[k][j] == float('inf'):
                        continue
                    dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])            
        min_count = float('inf')                    
        city_no = -1 
        for i in range(n):
            city_count = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    city_count += 1
            if city_count <= min_count:
                min_count = city_count
                city_no = i
                    
        return city_no          


                    

        