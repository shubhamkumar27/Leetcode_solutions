'''
Given a string containing just the characters '(' and ')', find the length of the longest 
valid (well-formed) parentheses substring.

Example 1:
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''

class Solution:
    def longestValidParentheses(self, s):
        if (len(s)==0 or s==None):
            return 0
        l = len(s)
        stack = [0]
        for i in range(1,l):
            if len(stack)==0:
                stack.append(i)
            elif s[i]==')' and s[stack[-1]]=='(':
                stack.pop()
            else:
                stack.append(i)
        print(stack)
        if stack==[]:
            return l
        maxm = max(stack[0],l-stack[-1]-1)
        for i in range(1, len(stack)):
            sub = stack[i]-stack[i-1]-1
            if sub > maxm:
                maxm = sub
        return maxm

############## METHOD 2 ###############
class Solution2:
    def longestValidParentheses(self, s):
        if (len(s)==0 or s==None):
            return 0
        l = len(s)
        stack = []
        maxm = 0
        for i in range(l):
            print(maxm,end=' ')
            if stack==[]:
                stack.append(i)
            elif s[i]==')' and s[stack[-1]]=='(':
                stack.pop()
                if stack==[]:
                    top = -1
                else:
                    top = stack[-1]
                maxm = max(i-top,maxm)
            else:
                stack.append(i)
            print(maxm)
        return maxm