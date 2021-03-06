# https://leetcode.com/problems/base-7/

# Given an integer, return its base 7 string representation.

# Example 1:

# Input: 100
# Output: "202"

# Example 2:

# Input: -7
# Output: "-10"

# Note: The input will be in range of [-1e7, 1e7]. 

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        out = ''
        if num < 0:
            num = -1*num
            flag = '-'
        else:
            flag = ''
        while num > 0:
            rem = num % 7
            num = num // 7
            out = str(rem) + out
        return flag+out

s = Solution()
num = int(input())
s.convertToBase7(num)
