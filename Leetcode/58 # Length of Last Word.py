# https://leetcode.com/problems/length-of-last-word/submissions/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        try:
            return len(s.split()[-1])
        except:
            return 0
        
