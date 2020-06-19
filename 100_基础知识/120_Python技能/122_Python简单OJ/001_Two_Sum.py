# https://leetcode.com/problems/two-sum/
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# Python版
class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        # 相当于java的map，取索引和对应值
        # 新建一个字典，key是数值，value是索引
        dictionary = {value: index for (index, value) in enumerate(nums)}
        for (i, v) in enumerate(nums):
            targetNum = target - v
            # 差的值在nums里可以取到，且不是当前的这个值
            if targetNum in dictionary and dictionary[targetNum] != i:
                return [i, dictionary[targetNum]]
# 解题是需要返回索引，所以建立一个字典，保存索引和值；
# 其次遍历list，找到可以组成当前目标值的索引。

# Time complexity : O(n^2)
# Space complexity : O(1).
