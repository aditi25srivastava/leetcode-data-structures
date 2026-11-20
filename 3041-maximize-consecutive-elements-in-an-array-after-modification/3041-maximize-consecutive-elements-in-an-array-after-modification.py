from collections import defaultdict
class Solution(object):
    def maxSelectedElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        dp = defaultdict(int)
        ans = 0
        for x in nums:
            dp[x + 1] = dp[x] + 1
            dp[x] = dp[x - 1] + 1
            ans = max(ans, dp[x], dp[x + 1])
        return ans    