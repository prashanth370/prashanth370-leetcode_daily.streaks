# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# import heapq

# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         # Create a min-heap to store the nodes
#         heap = []
        
#         # Add the first node of each list to the heap
#         for i, lst in enumerate(lists):
#             if lst:
#                 heapq.heappush(heap, (lst.val, i, lst))
        
#         dummy = ListNode(0)
#         curr = dummy
        
#         while heap:
#             val, i, node = heapq.heappop(heap)
#             curr.next = node
#             curr = curr.next
            
#             if node.next:
#                 heapq.heappush(heap, (node.next.val, i, node.next))
        
#         return dummy.next


import heapq
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Custom comparison for ListNode objects
        ListNode.__lt__ = lambda self, other: self.val < other.val
        
        # Initialize the min-heap with the head of each non-empty list
        heap = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
        
        # Create a dummy node to start the merged list
        dummy = ListNode(0)
        current = dummy
        
        # Merge the lists
        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next