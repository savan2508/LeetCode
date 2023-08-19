/*
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
s consists of lowercase English letters. */

const isAlmostPalindrome = function(s) {
    let left = 0, right = s.length -1;
    while (left < right) {
        if (s[left] !== s[right]){
            return validSubPalindrome(s, left + 1, right) || validSubPalindrome(s, left, right-1);    
        }
        left++;
        right--;
    }
    return true;
}

const validSubPalindrome = function(s, start, end) {
    while (start < end) {
        if (s[start] !== s[end]) {
            return false;
        }
        start++;
        end--;
    }
    return true;
}

const s1 = "abc";
const s2 = "abca";
const s3 = "aba";
const s4 = "cbbcc"
console.log(s1, isAlmostPalindrome(s1));
console.log(s2, isAlmostPalindrome(s2));
console.log(s3, isAlmostPalindrome(s3));
console.log(s4, isAlmostPalindrome(s4));