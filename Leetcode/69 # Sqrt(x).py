# https://leetcode.com/problems/sqrtx/

# Approach: 
# Apply Binary Search
# example for number 9
# 0 1 2 3 4 5 6 7 8 9
# left = 0, right = 9, mid = 4
# if 4**2 > 9 => yes , then right = mid - 1 = 3
# Now calculate mid = left + right // 2  ==> (0+3)//2 = > 1
# 1**2 < 9 , so left = mid + 1 i.e. 2
# so left = 2, right = 3,
# calculate mid 5//2 ==> 2
# 2**2 4< 9
# left = mid + 1 i.e. 3
# left =3, right = 3 , mid = (3+3)//2
# 3*3 = 9 < 9 (false)
# left = mid + 1 = 4
# now left > right (out of loop)
# so return left - 1 (i.e. 4-1 = 3)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        
        left = 0
        right = x
        while left < right:
            mid = (left+right)//2
            if mid**2 > x:
                right = mid - 1
            else:
                left = mid + 1
        return left-1
        