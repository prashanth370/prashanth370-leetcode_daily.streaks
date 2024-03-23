# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next  
            fast = fast.next.next 

        prev = None
        node = slow.next
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        slow.next = None
        
        p1, p2 = head, prev
        while p1 and p2:
            t1 = p1.next
            t2 = p2.next
            p1.next = p2
            p2.next = t1

            p1 = t1
            p2 = t2
