class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
    
        while len(s) > k:
            new_string = []
            for i in range(0, len(s), k):
                group = s[i : i+k]
                group_sum = sum(int(digit) for digit in group)
                new_string.append(str(group_sum))
            s = "".join(new_string)        
        return s


        