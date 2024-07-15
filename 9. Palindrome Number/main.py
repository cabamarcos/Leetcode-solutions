class Solution(object):
    def isPalindrome(self, x):
        if x<0 or (x != 0 and x % 10 == 0):
            return False

        invertido = 0
        while x>invertido:
            invertido = 10*invertido + x%10
            x //= 10
        
        return x == invertido or x == invertido//10
