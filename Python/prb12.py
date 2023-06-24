"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

 

Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

def intToRoman(num: int) -> str:
    output = ''
    while num > 0:
        if num // 1000 >= 1:
            output += 'M'
            num -= 1000
        elif num // 900 == 1:
            output += 'CM'
            num -= 900
        elif num // 500 == 1:
            output += 'D'
            num -= 500
        elif num // 400 == 1:
            output += "CD"
            num -= 400
        elif num // 100 >= 1:
            output += "C"
            num -= 100
        elif num // 90 == 1:
            output += 'XC'
            num -= 90
        elif num // 50 == 1:
            output += 'L'
            num -= 50
        elif num// 40 == 1:
            output += 'XL'
            num -= 40
        elif num // 10 >= 1:
            output += 'X'
            num -= 10
        elif num // 9 == 1:
            output += 'IX'
            num -= 9
        elif num // 5 == 1:
            output += 'V'
            num -= 5
        elif num // 4 == 1:
            output += 'IV'
            num -= 4
        elif num // 1 >= 1:
            output += 'I'
            num -= 1
    return output

num = 58
print(intToRoman(num))   
        