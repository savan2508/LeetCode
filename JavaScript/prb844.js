/*
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
 

Follow up: Can you solve it in O(n) time and O(1) space? */

const backSpaceCompareBruteForce = function (s, t) {
    const buildString = function (str) {
        const str_update = []
        for (let i = 0; i < str.length; i++) {
            if (str[i] !== '#') {
                str_update.push(str[i])
            } else {
                if (str_update.length > 0) {
                str_update.pop();
                }
            }
        }
        return str_update;
    }
    const s_update = buildString(s);
    const t_update = buildString(t);
    if (s_update.length !== t_update.length) {
        return false;
    } else {
        for (let i = 0; i < s_update.length; i++) {
            if (s_update[i] !== t_update[i]) {
                return false;
            }
        }
    }
    return true;
}

const backSpaceCompareTwoPointer = function (s, t) {
    let p1 = s.length - 1, p2 = t.length - 1;
    while (p1 >= 0 || p2 >= 0) {
        if (s[p1] === '#' || t[p2] === '#') {
            if (s[p1] === '#') {
                let backSpace = 2;
                while (backSpace > 0) {
                    p1--;
                    backSpace--;
                    let q = s[p1];
                    if (q === '#') {
                    backSpace = backSpace + 2;
                    }
                }
            }
            if (t[p2] === '#') {
                let backSpace = 2;
                while (backSpace > 0) {
                    p2--;
                    backSpace--;
                    if (t[p2] === "#") {
                        backSpace = backSpace + 2;
                    }
                }
            }
        } else {
            if (s[p1] !== t[p2]) {
                return false;
            } else {
                p1--;
                p2--;
            }
        }
    }
    return true;
} 

// const s = "ab#c", t = "ad#c";
const s = "ab##", t = "c#d#"
// const s = "a#c", t = "b"
// const s = "xywrrmp", t = "xywrrmu#p";

// console.log(backSpaceCompareBruteForce(s, t))
console.log(backSpaceCompareTwoPointer(s, t))