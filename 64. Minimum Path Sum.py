'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''
class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp_grid = grid[:][:]
        
        for i in range(1,m):
            dp_grid[i][0] += grid[i-1][0]

        for i in range(1,n):
            dp_grid[0][i] += dp_grid[0][i-1]

        for i in range(1,m):
            for j in range(1,n):
                dp_grid[i][j] += min(dp_grid[i-1][j],dp_grid[i][j-1])

        return dp_grid[-1][-1]
