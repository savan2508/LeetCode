/* 
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
s consists only of printable ASCII characters. */

const isValidPalindromeFromSide = function(s) {
    s = s.replace(/[^A-Za-z0-9]/g, "").toLowerCase();

    let left = 0; right = s.length -1;

    while (left < right) {
        if (s[left] !== s[right]) {
            return false
        }
        left++;
        right--;
    }
    return true;
}

const isValidPalindromeCenter = function (s) {
    s = s.replace(/[^A-Za-z0-9]/g, '').toLowerCase();

    let left = Math.floor(s.length / 2), right = left;

    if (s.length % 2 === 0) {
        left--;
    }
    while(left >= 0 && right < s.length) {
        if (s[left] !== s[right]) {
            return false
        }
        left--;
        right++;
    }
    return true;
}



const s = "A man, a plan, a canal: Panama";
console.log(isValidPalindrome(s))