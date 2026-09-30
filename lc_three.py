class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        us = set()
        curr = ""
        for c in s:
            if c not in curr:
                curr += c
            else:
                us.add(curr)
                curr = curr.partition(c)[2] + c
        us.add(curr)
        return max(len(substring) for substring in us)
