from collections import deque
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        start = "0000"
        if start in deadends:
            return -1
        queue = deque([(start, 0)])
        visited = {start}
        deadends = set(deadends)
        while queue:
            curr, steps = queue.popleft()
            if curr == target:
                return steps
            for i in range(4):
                digit = int(curr[i])
                for move in (-1, 1):
                    new_digit = (digit + move) % 10
                    next_status = curr[:i] + str(new_digit) + curr[i + 1 :]
                    if next_status not in visited and next_status not in deadends:
                        visited.add(next_status)
                        queue.append((next_status, steps + 1))
        return -1           


            

        