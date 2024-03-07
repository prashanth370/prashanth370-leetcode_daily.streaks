# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        # Move fast pointer two nodes at a time and slow pointer one node at a time
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # At this point, slow pointer is at the middle node
        return slow


        
        # even_node = []
        # odd_node = []
        # n = len(head)
        # for i in range(n):
        #     if i%2 !== 0:
        #         val = (n-1) // 2
        #         for j in range(val+1):
        #             j.append(val)

