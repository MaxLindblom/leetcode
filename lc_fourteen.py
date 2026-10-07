"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs or len(strs[0]) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        longest = ""
        prefix = strs[0][0]
        while all(s.startswith(prefix) for s in strs):
            longest = prefix
            if strs[0] == longest:
                break
            prefix += strs[0][len(longest)]
        return longest
