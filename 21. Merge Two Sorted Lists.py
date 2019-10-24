'''
Merge two sorted linked lists and return it as a new list. The new list should 
be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, h1, h2):
        res = ListNode(0)
        temp = res
        while(h1 and h2):
            if h1.val <= h2.val:
                temp.next = ListNode(h1.val)
                h1 = h1.next
            else:
                temp.next = ListNode(h2.val)
                h2 = h2.next
            temp = temp.next
        temp.next = h1 or h2
        return res.next