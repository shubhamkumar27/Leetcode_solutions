'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 
32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.
'''

class Solution:
    def reverse(self, x: int) -> int:
        s = 0
        # sign = 1
        # if x<0:
        #     sign = -1
        #     x = x*-1
        sign = [1,-1][x<0]
        x = abs(x)
        while(x!=0):
            temp = x%10
            s = 10*s + temp
            x = x//10
        ans = s*sign
        if -2**31<ans<2**31-1:
            return ans
        else:
            return 0