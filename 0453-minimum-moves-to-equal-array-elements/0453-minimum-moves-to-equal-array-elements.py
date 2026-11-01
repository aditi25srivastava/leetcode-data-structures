class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum = min(nums)
        total = sum(nums)
        n = len(nums)
        moves = total - (n * minimum)
        return moves
        