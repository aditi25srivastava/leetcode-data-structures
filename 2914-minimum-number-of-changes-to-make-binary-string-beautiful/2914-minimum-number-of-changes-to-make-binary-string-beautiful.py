class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        min_change = 0
        i = 0
        while i < len(s):
            if s[i] != s[i + 1]:
                min_change += 1
            i += 2
        return min_change        
