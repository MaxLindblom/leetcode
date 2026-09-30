"""
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


class Solution:
    def eval_array(self, nums: list[int], target: int) -> list[int]:
        for i, num in enumerate(nums):
            for j, other_num in enumerate(nums):
                if i is not j and num + other_num == target:
                    return [i, j]
        return []

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        unevaled_array = nums
        result = self.eval_array(unevaled_array, target)
        while not result:
            unevaled_array = unevaled_array[1:]
            result = self.eval_array(unevaled_array, target)
        return result
