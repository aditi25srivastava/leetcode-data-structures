class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        n = len(nums)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num) 
        min_sum = float('inf')    
        for i in range(n):
            for j in range(i,n):
                length = j - i + 1
                if l <= length <= r:
                    subarr_sum = prefix[j + 1] - prefix[i]
                    if subarr_sum > 0:
                        min_sum = min(min_sum, subarr_sum)
                      
        if min_sum == float('inf'):      
            return -1                        
        return min_sum 
        