class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        seen_b = False  
        for i in range(n):
            if s[i] == 'b':
                seen_b = True
            elif s[i] == 'a' and seen_b:
                return False
        return True               