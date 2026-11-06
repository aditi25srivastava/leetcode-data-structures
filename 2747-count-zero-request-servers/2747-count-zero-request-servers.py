class Solution(object):
    def countServers(self, n, logs, x, queries):
        """
        :type n: int
        :type logs: List[List[int]]
        :type x: int
        :type queries: List[int]
        :rtype: List[int]
        """
        logs.sort(key=lambda log: log[1])
        sorted_queries = sorted((q, i) for i,q in enumerate(queries))
        ans = [0] * len(queries)
        freq = {}
        left = 0
        right = 0
        active = 0
        for q, original_index in sorted_queries:
            left_time = q - x
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]
                freq[server] = freq.get(server, 0) + 1
                if freq[server] == 1:
                    active += 1
                right += 1
            while left < right and logs[left][1] < left_time:
                server = logs[left][0]
                freq[server] -= 1
                if freq[server] == 0:
                    active -= 1
                left += 1
            ans[original_index] = n - active
        return ans        




    
