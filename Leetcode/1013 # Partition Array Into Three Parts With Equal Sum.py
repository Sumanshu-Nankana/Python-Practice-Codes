# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

# Method-1
# Get the total sum of an array
# if sum will not be divided by 3 - it means we can't make 3 equal parts
# if we can divide, then we can make 3 equal parts, and get each part
# Now run loop, till we did not find sum equal to part
# if we found, store that index
# and run second loop from that and so on....
# if we found all 3 indexes - it means we divided into 3 parts

from typing import List
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        
        # get total sum of an array
        total_sum = sum(arr)
        
        # get one part sum
        part_sum = total_sum // 3
        
        # if sum will not be divided by 3, it means we can't divide into 3 parts return False
        if total_sum % 3 != 0:
            return False
        else:
            first, second, third, temp, length = 0, 0, 0, 0, len(arr)
            
            # check first sum, if found, store index
            for i in range(length):
                temp = temp + arr[i]
                if temp == part_sum:
                    first = i
                    second = i + 1
                    break
            
            
            # if it reaches end of loop already then no need to re-run loops
            if i!= length - 1:
                temp = 0
                # check second part
                for j in range(second, length):
                    temp = temp + arr[j]
                    if temp == part_sum:
                        second = j
                        third = j + 1
                        break
            else:
                return False
            
            print(second, j, temp, third)
            
            if j!= length - 1:
                temp = 0
                # check second part, but till end
                for k in range(third, length):
                    temp = temp + arr[k]
                if temp == part_sum:
                    return True
            else:
                return False
            
            if first!=0 and second!=0 and third!=0:
                return True
            else:
                return False
            
            
            
# Method-2
# instead of running 3 loops and putting so many IF-ELSE conditions and variables
# we can run single loop
# first sum = total_sum/3
# second_sum = 2*first_sum

# But only find 1st and second index
# if we find 1st and second index and 2nd index!= end
# then we divided in all partitions

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total_sum = sum(arr)
        part_sum = total_sum // 3
    
        if total_sum % 3 != 0:
            return False
        else:
            first_sum = part_sum
            second_sum = 2*part_sum
            length = len(arr)
            index1 = -1
            index2 = -1
            prevSum = 0
            
            for i in range(length):
                prevSum = prevSum + arr[i]
                if prevSum == first_sum and index1==-1:
                    index1 = i
                elif prevSum == second_sum and index1!=-1:
                    index2 = i
                    break
                
            if (index1!=-1) and (index2!=-1) and (index2!=length-1):
                return True
            else:
                return False
            