class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        count = 0
        for num in arr1:
            vaild = False
            for num2 in arr2:
                if abs(num - num2) <= d:
                    vaild = True
                    break
            if not vaild:
                count += 1
        return count                       
        




        
        