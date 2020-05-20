'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        diff = n-m

        dummy = ListNode(0)
        dummy.next = head
        cur, prev = head, dummy
        for i in range(m-1):
            cur = cur.next
            prev = prev.next
            
        h, t, r = reverse(cur, diff)
        prev.next = h
        t.next = r
        return dummy.next

def reverse(head, diff):
    if head==None or head.next==None:
        return (head, head, None)
    tail = head
    res = None
    while(diff>=0):
        temp = head.next
        head.next = res
        res = head
        head = temp
        diff-=1
    return (res, tail, head)