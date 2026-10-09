"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        results = []
        length = len(nums)
        for i in range(length - 2):
            n = nums[i]
            if n > 0:
                break
            if i > 0 and n == nums[i - 1]:
                continue
            if n + nums[i + 1] + nums[i + 2] > 0:
                break
            if n + nums[length - 1] + nums[length - 2] < 0:
                continue
            left = i + 1
            right = length - 1
            while left < right:
                sum = n + nums[left] + nums[right]
                if sum == 0:
                    results.append([n, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        return results
