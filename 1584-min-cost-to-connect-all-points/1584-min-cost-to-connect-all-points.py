class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        dist = [float('inf')] * n
        dist[0] = 0
        visited = [0] * n
        mst_dist = 0
        mst_sum = 0
        for _ in range(n):
            node = -1
            cur_dist = float('inf')
            for i in range(n):
                if not visited[i] and dist[i] < cur_dist:
                    cur_dist = dist[i]
                    node = i
            visited[node] = 1
            mst_sum += cur_dist
            for j in range(n):
                if not visited[j]:
                    distance = abs(points[node][0] - points[j][0]) + abs(points[node][1] - points[j][1])
                    dist[j] = min(dist[j], distance) 
        return mst_sum               


        