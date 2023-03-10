# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true
 

# Constraints:

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.

s1 = "egg"
t1 = "add"

s2 = "foo"
t2 = "bar"

s3 = "paper"
t3 = "title"

s4 = "badc"
t4 = "baba"




def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    dict1 = {}
    dict2 = {}
    for char1, char2 in zip(s,t):
        if char1 not in dict1.keys() and char2 not in dict2.keys():
            dict1[char1] = char2
            dict2[char2] = char1
        else:
            if char1 in dict1.keys():
                if dict1[char1] != char2:
                    return False
            elif char2 in dict2.keys():
                if dict2[char2] != char1:
                    return False
            else:
                continue
    return True

print(f"for s1 and t1 output: {isIsomorphic(s=s1, t=t1)}")
print(f"for s2 and t2 output: {isIsomorphic(s=s2, t=t2)}")
print(f"for s3 and t3 output: {isIsomorphic(s=s3, t=t3)}")
print(f"for s4 and t4 output: {isIsomorphic(s=s4, t=t4)}")
