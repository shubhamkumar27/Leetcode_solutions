'''
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
'''

from queue import Queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        fresh = 0
        q = Queue()
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    q.put([i,j])
                elif grid[i][j]==1:
                    fresh+=1
        
        direc = [-1,0,1,0,-1]
        temp = Queue()
        mins = 0
        
        while(1):
            while(not q.empty()):
                node = q.get()
                i,j = node[0], node[1]
                for k in range(4):
                    x = i + direc[k]
                    y = j + direc[k+1]
                    
                    if row>x>=0 and col>y>=0 and grid[x][y]==1:
                        grid[x][y]=2
                        temp.put([x,y])
                        fresh-=1
                        
            if temp.qsize()==0:
                break
            else:
                mins+=1
                q = temp
                temp = Queue()
                
        if fresh>0:
            return -1
        else:
            return mins
