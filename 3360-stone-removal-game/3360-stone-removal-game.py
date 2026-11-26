class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        requirement = 10
        alexTurn = True
        while n >= requirement:
            n -= requirement
            requirement -= 1
            alexTurn = not alexTurn
        if alexTurn == False:
            return True
        else:
            return False    
