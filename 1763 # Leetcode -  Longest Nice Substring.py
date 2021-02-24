# A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

# Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

# Example 1:

# Input: s = "YazaAay"
# Output: "aAa"
# Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
# "aAa" is the longest nice substring.

# Example 2:

# Input: s = "Bb"
# Output: "Bb"
# Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.

# Example 3:

# Input: s = "c"
# Output: ""
# Explanation: There are no nice substrings.

# Example 4:

# Input: s = "dDzeE"
# Output: "dD"
# Explanation: Both "dD" and "eE" are the longest nice substrings.
# As there are multiple longest nice substrings, return "dD" since it occurs earlier.

# Constraints:

#     1 <= s.length <= 100
#     s consists of uppercase and lowercase English letters.


class Solution:    
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) <= 1:
            return ""
        N = len(s)
        longest = ""
        def isNice(start, end):
            temp = set(s[start:end+1])
            for ch in temp:
                if ord(ch)>96 and ch.upper() not in temp:
                    return False
                elif ord(ch)<91 and ch.lower() not in temp:
                    return False
            return True  
        for start in range(N):
            for end in range(start+1, N):
                if isNice(start, end) and end-start+1 > len(longest):
                    longest = s[start:end+1]

        return longest

sol = Solution()
s = input()
s.longestNiceSubstring(s)