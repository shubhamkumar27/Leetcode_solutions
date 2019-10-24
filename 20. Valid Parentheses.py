'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
'''

class Solution:
    def isValid(self, s):
        l = [0]
        for c in s:
            if c=='(' or c=='{' or c=='[':
                l.append(c)
                # print(l)
            elif ( c==')' and l[-1]=='(' ) or ( c=='}' and l[-1]=='{' ) or ( c==']' and l[-1]=='[' ):
                l.pop()
            else:
                return False
        if l==[0]:
            return True