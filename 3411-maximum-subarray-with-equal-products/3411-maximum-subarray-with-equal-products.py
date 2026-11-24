from math import gcd,lcm
from typing import List
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        limit = lcm(*nums) * max(nums)
        ans = 0
        for i in range(n):
            prod = 1
            l = 1
            g = 0

            for j in range(i,n):
                prod = prod * nums[j]
                l = lcm(l,nums[j])
                g = gcd(g,nums[j])
                if prod == l * g:
                    ans = max(ans, j - i + 1)
                if prod > limit:
                    break    
        return ans   

                 
                
           