'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

depth = -2**31
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        global depth
        depth = -2**31
        if root==None:
            return 0
        dfs(root, 0)
        return depth
    
def dfs(root, level):
    global depth
    if root==None:
        return
    
    if root.left==None and root.right==None:
        depth = max(depth, level+1)
        
    dfs(root.left, level+1)
    dfs(root.right, level+1)