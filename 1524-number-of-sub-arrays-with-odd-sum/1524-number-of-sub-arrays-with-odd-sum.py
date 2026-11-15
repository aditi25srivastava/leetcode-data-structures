class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        prefix_sum = 0
        even_sum = 1
        odd_sum = 0
        ans = 0
        for num in arr:
            prefix_sum += num
            if prefix_sum  % 2 == 0:
                ans += odd_sum
                even_sum += 1
            else:
                ans += even_sum
                odd_sum += 1
        return ans % MOD            
        