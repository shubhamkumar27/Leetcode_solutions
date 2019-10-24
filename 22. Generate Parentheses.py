'''
Given n pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class Solution:
    
    def generateParenthesis(self, n):
        if n==0:
            return []
        return self.gphelper('', n, 0)
    
    def gphelper(self, cur, o_p_left, opened):
        if opened==0:
            return self.gphelper(cur+'(', o_p_left-1, opened+1)
        elif o_p_left==0:
            return [cur+')'*opened]
        else:
            return self.gphelper(cur+'(', o_p_left-1, opened+1) + self.gphelper(cur+')', o_p_left, opened-1)