"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads 
the same forward and backward. Alphanumeric characters include letters 
and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric 
characters. Since an empty string reads the same forward and backward, 
it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

def isPalindromeTwoPointerFromOut(s):
    left = 0
    right = len(s) - 1
    while left <= right:
        l = s[left]
        r = s[right]
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        else:
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
    return True

def isPalindrome(s: str) -> bool:
    temp = ""
    for char in s.lower():
        if char.isalpha() or char.isdigit():
            temp += char
    if temp != temp[::-1]:
        return False
    else:
        return True


s = "A man, a plan, a canal: Panama"
# s = "aba"
# s = "aabaa"
# s = "race a car"
# s = " "
# s =''

print(isPalindromeTwoPointerFromOut(s))
print(isPalindrome(s))