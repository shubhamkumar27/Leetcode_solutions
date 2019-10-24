'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?
'''

class Solution:
    def removeNthFromEnd(self, head, n, i=1):
        f = head
        b = head
        for i in range(n):
            if f : f = f.next 
            else: return None
        if(f==None):
            return head.next
        while(f.next):
            b = b.next
            f = f.next
        b.next = b.next.next
        return head