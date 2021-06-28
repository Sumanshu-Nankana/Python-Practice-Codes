# https://leetcode.com/problems/counting-elements/

from collections import Counter
from typing import List

class Solution:
    def countingElemets(self, arr: List) -> int:
        dic = Counter(arr)
        arr = set(arr)
        
        count = 0
        for ele in arr:
            if ele+1 in dic:
                count = count  + dic[ele]

        return count