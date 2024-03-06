# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        address = []
        curr = head
        while(curr is not None):
            address.append(curr)
            curr = curr.next
            if(curr in address):
                return True
        return False
        
        