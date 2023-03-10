# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.

def isSubsequence(s: str, t: str) -> bool:
    i = 0
    new_t = []
    t = list(t)
    for char in s:
        if char not in t:
            # print(f"i is {i} and char is {char} and t is {t}")
            return False
        elif char in t:
            i = t.index(char)
            # if i == 0:
            i += 1
            del t[0:i]
            # print(f"i is {i} and char is {char}")
            new_t.append(char)
    new_t = "".join(new_t)
    # print(f"new_t: {new_t}")
    if s == new_t:
        return True
    else:
        return False