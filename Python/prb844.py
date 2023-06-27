"""
844. Backspace String Compare

Companies
Given two strings s and t, return true if they are equal when both are 
typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?844. Backspace 
String Compare

Given two strings s and t, return true if they are equal when both are 
typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?
"""

def backspaceCompareBruteForce(s, t):
    s_update = []
    t_update = []
    for str in s:
        if str != '#':
            s_update.append(str)
        else:
            if len(s_update) > 0:
                s_update.pop()
    for str in t:
        if str != '#':
            t_update.append(str)
        else:
            if len(t_update) > 0:
                t_update.pop()
    return s_update == t_update

# s = "ab#c"
# t = "ad#c"

# s = "ab##"
# t = "c#d#"

s = "a#c"
t = "b"

print(backspaceCompareBruteForce(s, t))