'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

class Solution:
    def numTrees(self, n: int) -> int:
        if n<2:
            return 1
        dp = [-1]*(n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        return recursive(n, 0, dp)
        
        
def recursive(n, cur, dp):
    if dp[n]!=-1:
        return dp[n]
    
    for i in range(1, n+1):
        l=recursive(i-1, cur, dp)
        r=recursive(n-i, cur, dp)
        cur += l*r

    dp[n] = cur
    return dp[n]
        