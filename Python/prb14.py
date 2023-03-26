# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


def longestCommonPrefix(strs):

    short = min(strs, key=len) 
    for item in strs: 
        while len(short) > 0:
            if item.startswith(short): 
                break
            else:
                short = short[:-1] 
    return short

strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]

print(f"Solution for strs1: {longestCommonPrefix(strs=strs1)}")
print(f"Solution for strs2: {longestCommonPrefix(strs=strs2)}")