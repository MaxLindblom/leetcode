"""
Given a string s, return the longest palindromic substring in s.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome_from_center(i: int, j: int) -> str:
            if i < 0 or j >= len(s) or s[i] != s[j]:
                return s[i + 1 : j]
            return palindrome_from_center(i - 1, j + 1)

        best = ""
        for i in range(len(s)):
            best = max(
                best,
                palindrome_from_center(i, i + 1),
                palindrome_from_center(i, i),
                key=len,
            )

        return best
