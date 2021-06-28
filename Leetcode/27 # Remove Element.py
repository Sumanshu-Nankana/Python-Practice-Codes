# https://leetcode.com/problems/remove-element/

# approach
# we will use two pointers i & j
# and we will check if nums[j] == val, then we will increment it, and decrease count
# if nums[j] != val, it means we find out first element (which is not equal to val)
# put it at place of 'i' and increment both i & j

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j , count = 0, 0, len(nums)
        while j < len(nums):
            if nums[j] == val:
                j = j + 1
                count = count - 1
            else:
                nums[i] = nums[j]
                i = i + 1
                j = j + 1
        return count