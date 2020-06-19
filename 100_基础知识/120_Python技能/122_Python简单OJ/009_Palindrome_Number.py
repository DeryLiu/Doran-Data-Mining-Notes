# https://leetcode.com/problems/palindrome-number/
# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# Example 1:
# Input: 121
# Output: true

# Example 2:
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]

# 不将整数转为字符串来解决这个问题
class Solution2:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 负数一定不行
        if x < 0:
            return False
        original_x = x
        x = int(str(x)[::-1])
        return True if x == original_x else False

# Time complexity : O(log10(n))
# Space complexity : O(1).
