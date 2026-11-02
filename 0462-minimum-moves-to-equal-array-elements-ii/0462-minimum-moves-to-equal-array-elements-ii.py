class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        median = nums[n // 2]
        moves = 0
        for num in nums:
            moves += abs(num - median)
        return moves     
    