class Solution(object):
    def findSubtreeSizes(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: List[int]
        """
        n = len(parent)
        graph = [[] for _ in range(n)]
        for i in range(1,n):
            graph[parent[i]].append(i)
        last_seen = {}
        new_parent = list(parent)
        def dfs(node):
            previous = last_seen.get(s[node])
            if s[node] in last_seen:
                new_parent[node] = last_seen[s[node]]
            last_seen[s[node]] = node     
            for child in graph[node]:
                dfs(child)            
            if previous is not None:
                last_seen[s[node]] = previous
            else:
                del last_seen[s[node]]
        dfs(0)
        new_graph = [[] for _ in range(n)]
        for i in range(1, n):
            new_graph[new_parent[i]].append(i)
        ans = [1] * n
        def count_sizes(node):
            for child in new_graph[node]:
                ans[node] += count_sizes(child)
            return ans[node]
            
        count_sizes(0)
        return ans        
            
