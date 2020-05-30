'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        minHeap = []
        for head in lists:
            while(head):
                heapq.heappush(minHeap, head.val)
                head = head.next
        
        dummy = ListNode(-1)
        temp = dummy
        for i in range(len(minHeap)):
            node = ListNode(heapq.heappop(minHeap))
            temp.next = node
            temp = node
            
            
        return dummy.next
            