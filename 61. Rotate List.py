'''
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL

Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL

Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        if head==None:
            return head
        temp1 = head
        temp2 = head
        temp = head
        count=0
        while(temp):
            temp = temp.next
            count+=1
        k = k%count
        for i in range(k):
            temp2 = temp2.next
            
        if temp2==head:
            return head
        while(temp2.next!=None):
            temp1 = temp1.next
            temp2 = temp2.next
        temp2.next = head
        head = temp1.next
        temp1.next = None
        return head

############## BETTER EFFICIENCY ################
class Solution2:
    def rotateRight(self, head, k):
        if head == None or head.next == None: return head
        
        # calculate length
        l, p, prev = 0, head, None
        while p:
            l, p, prev = l+1, p.next, p
        if k % l == 0: return head
        step = l - k % l
        
        p = head
        # insert None
        for i in range(1, step):
            p = p.next
        p.next, prev.next, ret = None, head, p.next
        return ret