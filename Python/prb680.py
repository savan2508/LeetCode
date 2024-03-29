"""
680. Valid Palindrome II
Given a string s, return true if the s can be palindrome after deleting 
at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""

def validPalindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left <= right:
        if s[left] != s[right]:
            return valid_sub_palindrome(s, left+1, right) or valid_sub_palindrome(s, left, right-1)
        left += 1
        right -= 1
    return True
        
def valid_sub_palindrome(s, left, right):

    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True

s1 = "aba"
s2 = "abca"
print(s1, validPalindrome(s1))
print(s2, validPalindrome(s2))
