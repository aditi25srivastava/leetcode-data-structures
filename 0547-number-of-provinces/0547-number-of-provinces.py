class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        p = [i for i in range(n)]
        r = [0] * n
        def find_ult_par(node):
            if  node == p[node]:
                return node
            p[node] = find_ult_par(p[node])
            return p[node]
        def union(u, v):
            u = find_ult_par(u)
            v = find_ult_par(v)
            if u == v:
                return
            if r[u] < r[v] :
                p[u] = v
            elif r[v] < r[u]:
                p[v]  = u
            else:
                p[v] = u
                r[u] += 1 

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    union(i,j)
        count = 0
        for i in range(n):
            if p[i] == i:
                count += 1
        return count       

                               

        




            