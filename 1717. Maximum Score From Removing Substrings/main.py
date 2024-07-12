class Solution(object):
    def maximumGain(self, s, x, y):
        less = min(x,y)
        a = 0
        b = 0
        result = 0

        for i in s:
            if i>'b':
                result += min(a, b) * less
                a = 0
                b = 0
            elif i == 'a':
                if x < y and b > 0:
                    b -= 1
                    result += y
                else:
                    a +=1
            elif i == 'b':
                if x > y and a > 0:
                    a -= 1
                    result += x
                else:
                    b +=1

        result += min(a,b)*less
        return result


        
