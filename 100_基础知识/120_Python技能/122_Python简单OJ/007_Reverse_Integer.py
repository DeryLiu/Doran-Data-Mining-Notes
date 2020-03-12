# https://leetcode.com/problems/reverse-integer/
# Given a 32-bit signed integer, reverse digits of an integer.
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

        ret = int(('-' if x < 0 else '') + str(abs(x))[::-1].lstrip("0"))

        if abs(ret) > (2 ** 31 - 1):
            return 0

        return ret



# Time Complexity: O(log(x)).
# Space Complexity: O(1).
