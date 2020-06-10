'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    q = deque([(i,j)])
                    islands+=1
                    DFS(q,grid)
        return islands
                    
                    
def DFS(q,grid):
    r = len(grid)
    c = len(grid[0])
    
    dircn = [-1,0,1,0,-1]
    
    while(len(q)):
        i,j = q.pop()
        grid[i][j]="0"
        
        for k in range(4):
            x = i+dircn[k]
            y = j+dircn[k+1]
            
            if r>x>=0 and c>y>=0 and grid[x][y]=="1":
                q.append((x,y))
        