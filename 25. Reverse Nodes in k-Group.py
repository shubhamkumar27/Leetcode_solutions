'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number 
of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:
Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5

Note:
Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    ######## RECURSIVE ###########
    def reverseKGroup(self, head, k):
        if head==None:
            return head
        i=0
        res = None
        cur1 = head
        while(i<k and cur1):
            cur1 = cur1.next
            i+=1
        if i<k:
            return head
        i=0
        #res = None
        cur = head
        while i<k and cur:
            temp = cur.next
            cur.next = res
            res = cur
            cur = temp
            i += 1
        if cur:
            head.next = self.reverseKGroup(cur,k)
        return res
    
    ######## ITERATIVE #############
    def reverseKGroup_iter(self, head,k):
        jump = ListNode(0)
        dummy = jump
        l = head
        r = l
        #dummy.next = r
        while True:
            count = 0
            while count<k and r:
                r = r.next
                count += 1
            if count==k:
                pre , cur = r, l
                for _ in range(k):
                    temp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = temp
                jump.next = pre
                jump = l
                l=r
            else:
                return dummy.next