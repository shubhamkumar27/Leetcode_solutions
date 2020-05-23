'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head==None or head.next==None:
            return head
        flag = False
        prev = None
        temp = head
        if head.val<x:
            flag = True
            prev = head
        while(temp.next):
            if temp.next.val<x:
                current = temp.next
                temp.next = temp.next.next
                if flag:
                    current.next = prev.next
                    prev.next = current
                    prev = prev.next
                else:
                    current.next = head
                    head = current
                    prev = head
                    flag = True
                if temp.next==current:
                    temp = temp.next
            else:
                temp = temp.next
        return head
            

