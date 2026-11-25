class Solution:
    def smallestUniqueSubarray(self, nums):
        n = len(nums)

        if n == 0:
            return -1
        transitions = [{}]
        link = [-1]
        length = [0]
        occurrences = [0]

        last = 0

        for x in nums:
            cur = len(length)

            length.append(length[last] + 1)
            link.append(0)
            transitions.append({})
            occurrences.append(1)

            p = last

            while p != -1 and x not in transitions[p]:
                transitions[p][x] = cur
                p = link[p]

            if p == -1:
                link[cur] = 0

            else:
                q = transitions[p][x]

                if length[p] + 1 == length[q]:
                    link[cur] = q

                else:
                    clone = len(length)

                    length.append(length[p] + 1)
                    link.append(link[q])
                    transitions.append(transitions[q].copy())
                    occurrences.append(0)

                    while p != -1 and transitions[p].get(x) == q:
                        transitions[p][x] = clone
                        p = link[p]

                    link[q] = clone
                    link[cur] = clone

            last = cur

        size = len(length)

        count = [0] * (n + 1)

        for l in length:
            count[l] += 1

        for i in range(1, n + 1):
            count[i] += count[i - 1]

        order = [0] * size

        for v in range(size - 1, -1, -1):
            l = length[v]
            count[l] -= 1
            order[count[l]] = v

       
        for v in reversed(order):
            parent = link[v]

            if parent != -1:
                occurrences[parent] += occurrences[v]

        ans = n

        for v in range(1, size):
            if occurrences[v] == 1:
                shortest_length = length[link[v]] + 1
                ans = min(ans, shortest_length)

        return ans