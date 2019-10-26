'''
Given two integers dividend and divisor, divide two integers without using multiplication, 
division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3

Example 2:
Input: dividend = 7, divisor = -3
Output: -2

Note:
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit 
signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your 
function returns 231 − 1 when the division result overflows.
'''

class Solution:
    def divide(self, dividend, divisor):
        if dividend<0 and divisor<0 or dividend>0 and divisor>0:
            ans = 0
        else:
            ans = 1
        count = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while(abs(dividend)>=abs(divisor)):
            # print(abs(dividend),abs(divisor))
            dividend-=divisor
            count += 1
        if ans:
            return max(2**31-1,count - count - count, -2**31)
        else: return max(2**31-1,count, -2**31)