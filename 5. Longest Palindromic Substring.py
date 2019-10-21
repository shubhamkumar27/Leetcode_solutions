'''
Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        max_len=1
        l = len(s)
        dp_matrix = [[0 for i in range(l)] for i in range(l)]
        
        for i in range(l):
            dp_matrix[i][i]=1
            
        for i in range(l-1):
            if s[i]==s[i+1]:
                dp_matrix[i][i+1]=1
                max_len=2
                start=i
        
        k=3
        while k<=l:
            for i in range(l-k+1):
                j=i+k-1
                if s[i]==s[j] and dp_matrix[i+1][j-1]:
                    dp_matrix[i][j]=1
                    if k>max_len:
                        max_len=k
                        start = i
            k+=1
        return s[start:start+max_len]