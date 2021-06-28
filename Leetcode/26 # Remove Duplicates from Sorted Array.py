# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# It's mention - we don't need to use the Extra memory
# Also, we need to remove / replace the elements IN_PPLACE.
# Approach:

# take a Two pointers i & j (i at 0 and j at 1)
# one is slow pointer and other is fast pointer (we can say)
# So we will compare nums[i] with nums[j]
# if it's equal - menas duplicate, we increment J pointer (keeping I at same position)
# and also decrease count value (because we need to return number of non-duplicates or unique elements)

# if nums[i] == nums[j] - means no more duplicates, 
# So we will shift nums[j] at next position of nums[i] i.e. at nums[i+1]  (in this way, we are bringing all unique elements together)
# and then increment i and j both

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        count = len(nums)
        while j < len(nums):
            if nums[i] == nums[j]:
                j = j + 1
                count = count - 1 
            elif nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i = i + 1 
                j = j + 1
        return count