'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

depth = 2**31
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        global depth
        depth = 2**31
        if root==None:
            return 0
        dfs(root, 0)
        return depth
        
        
def dfs(root, dep):
    global depth
    if root==None:
        return
    if root.left==None and root.right==None:
        depth = min(depth, dep+1)
        return
    dfs(root.left, dep+1)
    dfs(root.right, dep+1)
##
        
        
