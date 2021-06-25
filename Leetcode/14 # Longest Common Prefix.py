# https://leetcode.com/problems/longest-common-prefix/

# Method-1
# Find Longest common prefix of first 2 string 
# Then find longest common prefix between output of 1st and 3rd string
# Then find longest common prefix between output of 2nd and 4th string and so on...
# in this way - at the end - we have Longest common prefix.
# Example ["leets", "leetcode", "leet", "leeds"]
# compare "leets" & leetcode ==> leet
# Now compare leet and leet ==> leet
# now compare leet and leeds ==> lee

class Solution:
    def longest(self, string1: str, string2: str) -> str:
        largest_string_prefix = ""
        length = min(len(string1), len(string2))
        for i in range(length):
            if string1[i] == string2[i]:
                largest_string_prefix = largest_string_prefix + string1[i]
            else:
                break
        return largest_string_prefix

    def longestCommonPrefix(self, strs: List[str]) -> str:
        t = strs[0]
        for s in range(len(strs)):
            t = self.longest(t, strs[s])
        
        return t
    
# Method-2
# Let's sort the string array(list)
# So it will get sorted on basis of prefix
# So, now we can only compare 1st and last string
# Because all string gets sorted, if first string starts with 'a' and last string starts with 'a'
# then definately all strings in middle starts with 'a'

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        out = ""
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                out = out + x
            else:
                break
        return out