'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
 

Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                if finder(i,j,board, word, visited):
                    return True
        return False
        

def finder(row, column, grid, word, visited):
    if word=='':
        return True
    # print(visited, row, column, word)
    if grid[row][column]==word[0] and (row, column) not in visited:
        visited.add((row, column))
        if len(grid)==1 and len(grid[0])==1 and len(word)==1:
            return True    
        if column+1<len(grid[0]):
            if finder(row, column+1, grid, word[1:], visited):
                return True
        if row+1<len(grid):
            if finder(row+1, column, grid, word[1:], visited):
                return True
        if column-1>=0:
            if finder(row, column-1, grid, word[1:], visited):
                return True
        if row-1>=0:
            if finder(row-1, column, grid, word[1:], visited):
                return True

        visited.remove((row, column))
            
    return False