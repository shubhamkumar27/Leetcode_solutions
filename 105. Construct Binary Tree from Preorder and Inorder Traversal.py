'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        indexes = {}
        for i in range(len(inorder)):
            indexes[inorder[i]] = i
        root = createTree(preorder, inorder, indexes, 0)
        return root
        
def createTree(preorder, inorder, indexes, start):
	if len(inorder)==0 or len(preorder)==0:
		return None
	val = preorder.pop(0)
	index = indexes[val]
	root = TreeNode(val)
	root.left = createTree(preorder, inorder[0:index-start], indexes, start)
	root.right = createTree(preorder, inorder[index+1-start:], indexes, index+1)
	return root
    