from collections import deque
class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        ans = 0
        right = n - 1
        operations = 0
        stack = deque()
        for left in range(n-1, -1, -1):
            count = 1
            while stack and stack[-1][0] <= nums[left]:
                value,group_count = stack.pop()
                operations += (nums[left] - value) * group_count
                count += group_count
            stack.append([nums[left], count])
            while operations > k:
                stack[0][1] -= 1
                operations -= stack[0][0] - nums[right]
                if stack[0][1] == 0:
                    stack.popleft()
                right -= 1
            ans += right - left + 1
        return ans



        