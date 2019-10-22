'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads 
the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. 
Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        ######## USING STRING ###########
        s = str(x)
        l = len(s)
        i,j = 0,l-1
        while(i < j):
            if s[i]==s[j]:
                i += 1
                j -= 1
            else:
                return False
        if (i==j or i>j):
            return True

        ######## WITHOUT STRING ################
        reverse = 0
        y = x
        while x>0:
            temp = x%10
            reverse = reverse*10 + temp
            x = x//10
        if y==reverse:
            return True
        else:
            return False