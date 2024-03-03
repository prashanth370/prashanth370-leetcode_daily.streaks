# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # step1:  create a dummy node so that we can move dummy.next= head
        dummy = ListNode()
        dummy.next = head

        # step2: assign two pointers at very beginning of list
        ptr1 = dummy
        ptr2 = dummy

        #  step3: now move ptr2 to n spaces where n = depends on example test cases
        for i in range(n):
                ptr2 = ptr2.next

        # step4: now move both pointers, untill the next of ptr2 is null
        while ptr2.next is not None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next 

        # step5; now we have to remove the node next of ptr1 
        ptr1.next = ptr1.next.next

        return dummy.next

    # it takes time complexity as O(n) and space complexity as O(1)
