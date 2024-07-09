"""
https://leetcode.com/problems/reverse-integer/

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        string_x = str(x)
        
        if x >= 0:
            reverse_string_x = string_x[::-1]
            reversed_value =  int(reverse_string_x)
        else:
            reverse_string_x = string_x[::-1][:-1]
            reversed_value = int(reverse_string_x) * -1

        if not (-2147483648 <= int(reverse_string_x) <= 2147483647):
            return 0
        else:
            return reversed_value


        