'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
'''

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        x = 1
        q2,q3,q5 = [], [], []
        
        for i in range(1,n):
            q2.append(2*x)
            q3.append(3*x)
            q5.append(5*x)
            
            x = min(q2[0], q3[0], q5[0])
            
            if x==q2[0]:
                q2.pop(0)
            
            if x==q3[0]:
                q3.pop(0)
                
            if x==q5[0]:
                q5.pop(0)
                
                
        return x
        