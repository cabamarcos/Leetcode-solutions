class Solution(object):
    def romanToInt(self, s):
        dict_rom = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        num = 0

        for i in range(len(s)):
            curr_val = dict_rom[s[i]] 
            next_val = dict_rom[s[i+1]] if i+1 < len(s) else 0

            if next_val > curr_val:
                num -= curr_val
            else:
                num += curr_val

        return num
        
