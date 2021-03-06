'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the 
bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
Note: m and n will be at most 100.

Example 1:
Input: m = 3, n = 2
Output: 3

Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3
Output: 28
'''

class Solution:

    ## DYNAMIC PROGRAMMING
    def uniquePaths(self, m, n):
        dp_grid = [[1 for i in range(n)] for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp_grid[i][j] = dp_grid[i-1][j]+dp_grid[i][j-1]
        return dp_grid[-1][-1]

    ## MATHS
    def uniquePaths2(self, m, n):
        m_fact = self.factorial(m-1)
        n_fact = self.factorial(n-1)
        mn_fact = self.factorial(m+n-2)
        ans = mn_fact//(m_fact*n_fact)
        return ans
    
    def factorial(self,m):
        fact = 1
        for i in range(1,m+1):
            fact *= i
        return fact