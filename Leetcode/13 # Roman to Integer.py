# https://leetcode.com/problems/roman-to-integer/

# Method-1
# Store single digits in dictionary
# and check for exceptional cases where left digit is < right digit i.e. IV, IX etc i.e. 4, 9, 40, 90, 400, 900

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        
        start = len(s) - 1
        output = 0
        
        for i in range(start, -1, -1):
            if (s[i] == 'I') and (i < start) and (s[i+1] == 'V' or s[i+1] == 'X'):
                output = output - dic.get(s[i], 0)
            elif (s[i] == 'X') and (i < start) and (s[i+1] == 'L' or s[i+1] == 'C'):
                output = output - dic.get(s[i], 0)
            elif (s[i] == 'C') and (i < start) and (s[i+1] == 'D' or s[i+1] == 'M'):
                output = output - dic.get(s[i], 0)
            else:
                output = output + dic.get(s[i], 0)
        return output
    
# Method-1
# Store single digits in dictionary, also stores the exceptional digits in dictionary as well

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'XD':400,
            'XM':900
        }
        
        i, output, length = 0, 0, len(s)
        
        while True:
            try:
                if s[i:i+2] in dic:
                    output = output + dic.get(s[i:i+2], 0)
                    i = i + 2
                else:
                    output = output + dic.get(s[i], 0)
                    i = i + 1
            except:
                break
        
        return output
    
# Method-3
# Same as Method-2 (only) - with a small change in loop

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
        }
        
        i, output, length = 0, 0, len(s)
        
        while i < length:
            # i.e. we will check 2 numbers if it exists then we will take that number
            # and increment by 2 also
            if i+1 < len(s) and s[i:i+2] in dic:
                output = output + dic.get(s[i:i+2], 0)
                i = i + 2
            # else scan one by one number and increment by one
            else:
                output = output + dic.get(s[i], 0)
                i = i + 1
        return output