# https://leetcode.com/problems/palindrome-number/

# Method-1
# By converting into String
# But in question, it's mention - DO NOT do by converting into STRING
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x == int(str(x)[::-1]): 
            return True 
        else: 
            return False
        
# Method-2
# by reversing the whole number and then comparing with original number
# below will work for the test case provided in Leetcode
# but this is not good solution, because
# if Reversed number is > INT_MAX, we will hit integer overflow problem
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        temp = x
        rev = 0
        while x > 0:
            quo, rem = divmod(x, 10)
            rev = rev * 10
            rev = rev + rem
            x = quo
        
        if temp == rev: 
            return True 
        else: 
            return False
        
# Method-3
# To prevent the Integer overflow problem

# we can only revert half of the number, and commpare it with other half
# if it's equal then it's palindrome
# example 1221 ==> we will revert only '21' (last half) ==> 12 = reverted_Number (store in some variable)
# and then we will compare it with first half i.e. 12 (first 2 numbers)
# if it's equal then it's palindrome

# for the odd length numbers, example, 12321
# we don't care about middle number
# so after reverting last half (i.e. last 3 digits 321, we will get 123 (will store in some variable)
# but first half is 12
# we will get rid of extra 3 by dividing by 10

# Now, how we will know, when we reached half
# we will compare remaining quotient with the reverted number.
# if it's less than we reached or cross half.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # all negative numbers are not palindrome
        if (x < 0):
            return False
        
        # 10, 100, 1000 etc are also not palindrom
        if (x%10 == 0 and x !=0):
            return False
        
        # checking for all others numbers
        # and we will check only last half number
        revertedNumber = 0
        while (x > revertedNumber):
            quo, rem = divmod(x, 10)
            revertedNumber = revertedNumber*10 + rem
            x = quo
        
        # in case of odd numbers, we can get rid of the middle number by //10
        return (x == revertedNumber) or x == revertedNumber//10