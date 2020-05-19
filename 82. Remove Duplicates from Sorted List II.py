'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        
        if head.next.val == head.val:
            temp = head
            head = head.next
            while(head):
                if head.val!=temp.val:
                    if head.next==None:
                        break
                    elif head.val!=head.next.val:
                        break
                temp = temp.next
                head = head.next
            
            if head==None:
                return head
            
        pointer = head
        prev = head
        temp = head.next
        while(temp):
            if prev.val!=temp.val:
                if temp.next==None or temp.next.val!=temp.val:
                    pointer.next = temp
                    pointer = temp
            prev = prev.next
            temp = temp.next
        pointer.next = temp
        return head
    