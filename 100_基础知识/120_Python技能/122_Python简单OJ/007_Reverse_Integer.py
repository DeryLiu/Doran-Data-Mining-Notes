# https://leetcode.com/problems/reverse-integer/
# Given a 32-bit signed integer, reverse digits of an integer.
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转
# Example 1:
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21

import math
class Solution:
    def reverse(self, x: 'int') -> 'int':
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        # 符号单独提出，然后用字符串的倒序，并去除首位的0
        ret = int(('-' if x < 0 else '') + str(abs(x))[::-1].lstrip("0"))
        # 溢出检查
        if abs(ret) > (2 ** 31 - 1):
            return 0
        return ret


# Time Complexity: O(log(x)).
# Space Complexity: O(1).
