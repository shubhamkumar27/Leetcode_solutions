'''
Given two non-negative integers num1 and num2 represented as strings, return the product of 
num1 and num2, also represented as a string.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

class Solution:
    def multiply(self, num1, num2):
        m = len(num1)
        n = len(num2)
        arr = [0]*(m+n)
        carry = 0
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                arr[i+j+1] += (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0'))
        
        for i in range(len(arr)-1,-1,-1):
            arr[i] += carry
            carry = arr[i]//10
            arr[i] = str(arr[i]%10)
        
        for i in range(len(arr)):
            if arr[i]!= '0' or i==len(arr)-1:
                break
                  
        return ''.join(arr[i:])