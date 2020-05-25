'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
 '''

 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
#         if len(nums)==0:
#             return None
        
#         mid = len(nums)//2
        
#         node = TreeNode(nums[mid])
        
#         node.left = self.sortedArrayToBST(nums[:mid])
#         node.right = self.sortedArrayToBST(nums[mid+1:])
        
#         return node

test = int(input())
for _ in range(test):
    n = int(input())
    seq = list(map(int, input().split()))
    ingred = set()
    freq = set()
    i = 0
    flag = True
    while(i<n):
        start = seq[i]
        f = 0
        # print(start, ingred,freq, i, f)
        if start in ingred:
            print('NO')
            break
        while(i<n and seq[i]==start):
            f+=1
            i+=1
        # print(start, ingred,freq, i, f)
        if f in freq:
            print('NO')
            break
        else:
            ingred.add(start)
            freq.add(f)
            i-=1
        i+=1
    print('YES')
        
  