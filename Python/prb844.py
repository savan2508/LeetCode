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

def backSpaceCompareTwoPointer(s, t):
    s_length = len(s) - 1
    t_length = len(t) - 1
    while s_length >= 0 or t_length >= 0:
        if s_length >= 0:
            if s[s_length] == '#':
                back_space = 2
                while back_space > 0:
                    s_length -= 1
                    back_space -= 1
                    if s[s_length] == '#' and s_length >= 0:
                        back_space += 2

        if t_length >= 0:
            if t[t_length] == '#':
                back_space = 2
                while back_space > 0:
                    t_length -= 1
                    back_space -= 1
                    if t[t_length] == "#" and t_length >= 0:
                        back_space += 2

        if s_length >= 0 and t_length >= 0:
            if s[s_length] != t[t_length]:
                return False
            else:
                s_length -= 1
                t_length -= 1
        elif s_length >= 0 and t_length < 0:
            if s[s_length] != '#':
                return False
        elif t_length >= 0 and s_length < 0:
            if t[t_length] != '#':
                return False

    return True

s = "ab#c"
t = "ad#c"

# s = "ab##"
# t = "c#d#"

# s = "a#c"
# t = "b"

# s = "a##c"
# t = "#a#c"

# s = "xywrrmp"
# t = "xywrrmu#p"

# s = "bxj##tw"
# t = "bxj###tw"

print(backSpaceCompareTwoPointer(s, t))