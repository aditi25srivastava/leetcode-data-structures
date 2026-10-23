from collections import deque
from collections import defaultdict
class Solution(object):
    def minimumTime(self, n, relations, time):
        """
        :type n: int
        :type relations: List[List[int]]
        :type time: List[int]
        :rtype: int
        """
        graph = defaultdict(list)
        indegree = [0] * (n + 1)
        for  prevCourse, course in relations:
                graph[prevCourse].append(course)
                indegree[course] += 1
        queue = deque()
        finsh_time =  [0] + time[:]
        for course in range(1, n + 1):
                if indegree[course] == 0:
                    queue.append(course)

        while queue:
            node = queue.popleft()
            for next_course in graph[node]:
                finsh_time[next_course] = max(finsh_time[next_course], finsh_time[node] + time[next_course - 1])
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        return max(finsh_time[1:])                        