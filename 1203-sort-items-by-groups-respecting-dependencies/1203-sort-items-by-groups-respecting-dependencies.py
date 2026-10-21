from collections import deque
class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        itemGraph = [[] for _ in range(n)]
        groupGraph = [[] for _ in range(m)]

        itemIndegree = [0] * n
        groupIndegree = [0] * m

        for item in range(n):
            for prev in beforeItems[item]:
                if group[prev] == group[item]:
                    itemGraph[prev].append(item)
                    itemIndegree[item] +=  1
                else:
                    groupGraph[group[prev]].append(group[item])
                    groupIndegree[group[item]] += 1
        def toposort(graph, indegree):
            queue = deque()
            for i in range(len(indegree)):
                if indegree[i] == 0:
                    queue.append(i)
            order = []
            while queue:
                node = queue.popleft()
                order.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

            if len(order) != len(indegree):
                return []

            return order
        groupOrder = toposort(groupGraph, groupIndegree)
        if not groupOrder:
            return []
        itemOrder = toposort(itemGraph, itemIndegree)
        if not itemOrder:
            return []
        groupItems = [[] for _ in range(m)]   
        for item in itemOrder:
            groupItems[group[item]].append(item)
        answer = []
        for g in groupOrder:
            answer.extend(groupItems[g])
        return answer         



        