"""Seven different symbols represent Roman numerals with the following values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Roman numerals are formed by appending the conversions of decimal place values from highest to lowest.
Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input,
append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example,
4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times.
If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.
"""


def romanise(digit: int, ten: str, five: str, one: str) -> str:
    if 4 < digit < 9:
        return five + (digit % 5) * one
    if digit < 4:
        return digit * one
    if digit == 9:
        return one + ten
    return one + five


class Solution:
    def intToRoman(self, num: int) -> str:
        digits = [0, 0, 0, 0]
        i = 0
        while num > 0:
            digit = num % 10
            digits[i] = digit
            i += 1
            num //= 10

        roman = ""
        roman += digits[3] * "M"
        if digits[2]:
            roman += romanise(digits[2], "M", "D", "C")
        if digits[1]:
            roman += romanise(digits[1], "C", "L", "X")
        if digits[0]:
            roman += romanise(digits[0], "X", "V", "I")

        return roman
