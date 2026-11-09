import heapq
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        m = len(heights)
        n = len(heights[0])
        dist = [[float("inf")] * n for _ in range(m)]
        dist[0][0] = 0
        qp = [(0,0,0)]
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
        while qp:
            effort, row, col = heapq.heappop(qp)
            if row == m - 1 and col == n - 1:
                return effort
            if effort > dist[row][col]:
                continue  
            for i in range(4):
                newr = row + dr[i]
                newc = col + dc[i]                  
                if 0 <= newr < m and 0 <= newc < n:
                    diff = abs(heights[row][col] - heights[newr][newc])
                    newEffort = max(effort, diff)
                    if newEffort < dist[newr][newc]:
                        dist[newr][newc] = newEffort
                        heapq. heappush(qp,(newEffort, newr,newc))
        return 0                
            
