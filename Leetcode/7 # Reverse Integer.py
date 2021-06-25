# https://leetcode.com/problems/reverse-integer/

# Method-1
class Solution:
    def reverse(self, x: int) -> int:
        output = 0
        temp = x
        if x == 0: return 0
        if x < 0: x = x * (-1)
        
        while (x > 0):
            quo = x//10
            rem = x%10
            x = quo
            output = output * 10
            output = output + rem
            if output > 2**31: return 0

        if temp < 0:
            return -output
        else:
            return output
        
# Method-2
# we can directly use the divmod function (which takes 2 args numenator and denominator)
# and return quotient and remainder
class Solution:
    def reverse(self, x: int) -> int:
        output = 0
        temp = x
        if x == 0: return 0
        if x < 0: x = x * (-1)
        
        while (x > 0):
            quo, rem = divmod(x, 10)
            x = quo
            output *= 10
            output += rem
            if output > 2**31: return 0

        if temp < 0:
            return -output
        else:
            return output
        
# Method-3
# Convert number into string and reverse the string using slicing
        
class Solution:
    def reverse(self, x: int) -> int:
        temp = x
        if x == 0: return 0
        if x < 0: x = x * (-1)
        
        output = int(str(x)[::-1])
        if output > 2**31: return 0
        if temp < 0:
            return -output
        else:
            return output