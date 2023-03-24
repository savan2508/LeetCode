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

def isIsomorphic(s: str, t: str) -> bool:

    dict_1 = {}
    for char1, char2 in zip(s,t):
        if char1 not in dict_1.keys():
            dict_1[char1] = char2
        else:
            if dict_1[char1] != char2:
                return False
            else:
                continue
    dict_2 = {}
    for char1, char2 in zip(s,t):
        if char2 not in dict_2.keys():
            dict_2[char2] = char1
        else:
            if dict_2[char2] != char1:
                return False
            else:
                continue

    dic1_keys = [keys for keys in dict_1.keys()]
    dict2_keys = [keys for keys in dict_2.keys()]
    dict1_values = [values for values in dict_1.values()]
    dict2_values = [values for values in dict_2.values()]

    if dic1_keys == dict2_values and dict1_values == dict2_keys:
        return True
    else:
        return False
    

s = "badc"
t = "baba"
# s = "egg"
# t = "add"

print(isIsomorphic(s, t))