class Solution:
    def isValid(self, nums, k):
        n = len(nums)
        l, r = 0, 0

        mp = {}

        mod = 1000000007
        base = 100001
        p = 1
        hash = 0
        for i in range(k - 1):
            p = (p * base) % mod
        while r < n:
            hash = (hash * base + nums[r]) % mod

            if r - l + 1 == k:
                mp[hash] = mp.get(hash, 0) + 1
                hash = (hash - nums[l] * p % mod + mod) % mod

                l += 1

            r += 1
        for e in mp.values():
            if e == 1:
                return True

        return False

    def smallestUniqueSubarray(self, nums):
        n = len(nums)
        l = 1
        h = n
        ans = n
        while l <= h:
            m = l + (h - l) // 2

            if self.isValid(nums, m):
                h = m - 1
                ans = m
            else:
                l = m + 1
        return ans