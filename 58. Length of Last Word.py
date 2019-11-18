'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
return the length of last word in the string.
If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:
Input: "Hello World"
Output: 5
'''

class Solution:
    def lengthOfLastWord(self, s):
        l = s.split(' ')
        print(l)
        if len(l)==0:
            return 0
        for i in range(len(l)-1,-1,-1):
            if len(l[i])>0:
                return len(l[i])
        return 0
