class Solution(object):
    def minimizeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        score1 = nums[n-1] - nums[2]
        score2 = nums[n-2] - nums[1]
        score3 = nums[n-3] - nums[0]

        score = min(score1, score2, score3)
        return score

        