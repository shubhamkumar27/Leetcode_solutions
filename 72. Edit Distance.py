'''
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1 for i in range(len(word2))] for j in range(len(word1))]
        i = len(word1)-1
        j = len(word2)-1
        return recursion(word1, word2, i, j, dp)
        
        
def recursion(w1, w2, i, j, dp):
    if i<0 or j<0:
        return abs(i-j)

    if dp[i][j]!=-1:
        return dp[i][j]
    
    if w1[i]==w2[j]:
        return recursion(w1, w2, i-1, j-1, dp)
    a = 1+recursion(w1, w2, i, j-1, dp)
    b = 1+recursion(w1, w2, i-1, j, dp)
    c = 1+recursion(w1, w2, i-1, j-1, dp)
    dp[i][j] = min(a,b,c)
    
    return min(a,b,c)