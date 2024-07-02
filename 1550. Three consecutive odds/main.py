class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        nOdds = 0
        for i in arr:
            if i % 2 == 1:
                nOdds += 1
                if nOdds == 3:
                    return True
            else:
                nOdds = 0
        return False
        
