# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b in ('(', '{', '['):
                stack.append(b)
            else:
                if len(stack) > 0:
                    rem = stack.pop()
                    if (rem == '(' and b !=')'):
                        return False
                    if (rem == '{' and b !='}'):
                        return False
                    if (rem == '[' and b !=']'):
                        return False
                else:
                    return False
        
        if len(stack)==0:
            return True
        else:
            return False