'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the 
bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2

Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp_grid=[]
        if obstacleGrid[0][0]==1:
            return 0
        j=0
        while(j<m) and (not obstacleGrid[j][0]):
            dp_grid.append([1]+[0]*(n-1))
            j+=1
            
        for i in range(j,m):
            dp_grid.append([0]*n)
        
        for i in range(n):
            if not obstacleGrid[0][i]:
                dp_grid[0][i]=1
            else:
                break
        print(dp_grid)
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]:
                    dp_grid[i][j] = 0
                else:
                    dp_grid[i][j] = dp_grid[i-1][j]+dp_grid[i][j-1]
        return dp_grid[-1][-1]