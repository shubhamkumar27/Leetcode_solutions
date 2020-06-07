'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
'''

from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        dircn = [-1,0,1,0,-1]
        maxArea = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    area = 0
                    grid[i][j]=0
                    q = deque([(i,j)])
                    while len(q)>0:
                        area+=1
                        r, c = q.pop()
                        
                        for k in range(4):
                            x = r+dircn[k]
                            y = c+dircn[k+1]
                            
                            if row>x>=0 and col>y>=0 and grid[x][y]==1:
                                grid[x][y]=0
                                q.append((x,y))

                    maxArea = max(maxArea, area)
                    
        return maxArea
