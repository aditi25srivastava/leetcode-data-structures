class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
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

        cntExtra = 0
        for u ,v in connections:
            if find_ult_par(u) == find_ult_par(v):
                cntExtra += 1
            else:
                union(u, v)

        cntC = 0
        for i in range(n):
            if p[i] == i:
                cntC += 1
            
        ans = cntC - 1
        if cntExtra >= ans:
            return ans
        return -1                
