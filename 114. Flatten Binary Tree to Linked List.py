'''
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        flatRecurse(root)
        
def flatRecurse(root):
    if root==None:
        return None
    
    right = flatRecurse(root.right)
    left = flatRecurse(root.left)
    
    if root.left:
        temp = root.right
        root.right = root.left
        left.right = temp
        root.left = None
        if right:
            return right
        else:
            return left
    
    else:
        if root.right==None:
            return root
        else:
            return right
