"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        reversed = 0
        orig = x
        while x > 10:
            digit = x % 10
            reversed = reversed * 10 + digit
            x //= 10

        return reversed == orig
